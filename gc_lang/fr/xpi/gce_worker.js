// JavaScript

// Grammar checker engine
// PromiseWorker
// This code is executed in a separate thread (×20 faster too!!!)

// Firefox WTF: it’s impossible to use require as in the main thread here,
// so it is required to declare a resource in the file “chrome.manifest”.


"use strict";

// copy/paste
// https://developer.mozilla.org/en-US/docs/Mozilla/JavaScript_code_modules/PromiseWorker.jsm

importScripts("resource://gre/modules/workers/require.js");
let PromiseWorker = require("resource://gre/modules/workers/PromiseWorker.js");

// Instantiate AbstractWorker (see below).
let worker = new PromiseWorker.AbstractWorker();

worker.dispatch = function(method, args = []) {
  // Dispatch a call to method `method` with args `args`
  return self[method](...args);
};
worker.postMessage = function(...args) {
  // Post a message to the main thread
  self.postMessage(...args);
};
worker.close = function() {
  // Close the worker
  self.close();
};
worker.log = function(...args) {
  // Log (or discard) messages (optional)
  dump("Worker: " + args.join(" ") + "\n");
};

// Connect it to message port.
self.addEventListener("message", msg => worker.handleMessage(msg));

// end of copy/paste


// no console here, use “dump”

let gce = null; // module: grammar checker engine
let text = null;
let tkz = null; // module: tokenizer
let lxg = null; // module: lexicographer
let helpers = null;

let oTokenizer = null;
let oDict = null;
let oLxg = null;

function loadGrammarChecker (sGCOptions="") {
    if (gce === null) {
        gce = require("resource://grammalecte/fr/gc_engine.js");
        helpers = require("resource://grammalecte/helpers.js");
        text = require("resource://grammalecte/text.js");
        tkz = require("resource://grammalecte/tokenizer.js");
        lxg = require("resource://grammalecte/fr/lexicographe.js");
        oTokenizer = new tkz.Tokenizer("fr");
        helpers.setLogOutput(worker.log);
        gce.load();
        oDict = gce.getDictionary();
        oLxg = new lxg.Lexicographe(oDict);
        if (sGCOptions !== "") {
            gce.setOptions(helpers.objectToMap(JSON.parse(sGCOptions)));
        }
        // we always retrieve options from the gce, for setOptions filters obsolete options
        return gce.getOptions()._toString();
    }
}

function parse (sText, sLang, bDebug) {
	let lGrammarErr = gce.parse(sText, sLang, bDebug);
	return JSON.stringify(lGrammarErr);
}

function parseAndTag (sText, iParagraph, sLang, bDebug) {
    sText = text.addHtmlEntities(sText);
    let lSpellErr = [];
    for (let oToken of oTokenizer.genTokens(sText)) {
        if (oToken.sType === 'WORD' && !oDict.isValidToken(oToken.sValue)) {
            lSpellErr.push(oToken);
        }
    }
    let lGrammarErr = gce.parse(sText, sLang, bDebug);
    let sHtml = text.tagParagraph(sText, iParagraph, lGrammarErr, lSpellErr);
    return sHtml;
}

function parseAndGenerateParagraph (sText, iParagraph, sLang, bDebug) {
    return text.createHTMLBlock(parseAndTag(sText, iParagraph, sLang, bDebug), iParagraph);
}

function getOptions () {
    return gce.getOptions()._toString();
}

function setOptions (sGCOptions) {
    gce.setOptions(helpers.objectToMap(JSON.parse(sGCOptions)));
    return gce.getOptions()._toString();
}

function setOption (sOptName, bValue) {
    gce.setOptions(new Map([ [sOptName, bValue] ]));
    return gce.getOptions()._toString();
}

function resetOptions () {
    gce.resetOptions();
    return gce.getOptions()._toString();
}


function fullTests (sGCOptions="") {
    if (!gce || !oDict) {
        return "# Error: grammar checker or dictionary not loaded."
    }
    let dMemoOptions = gce.getOptions();
    if (sGCOptions) {
        gce.setOptions(helpers.objectToMap(JSON.parse(sGCOptions)));
    }
    let tests = require("resource://grammalecte/tests.js");
    let oTest = new tests.TestGrammarChecking(gce);
    let sAllRes = "";
    for (let sRes of oTest.testParse()) {
        dump(sRes+"\n");
        sAllRes += sRes+"<br/>";
    }
    gce.setOptions(dMemoOptions);
    return sAllRes;
}


// Lexicographer

function analyzeWords (sText) {
    return oLxg.analyzeText(sText);
}
