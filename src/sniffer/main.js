function notify(arg){
	window.open(arg);
}

chrome.webRequest.onBeforeRequest.addListener(
    details => {
		browser.tabs.query({ active: true, lastFocusedWindow: true }, ([tab]) => {
			if (tab)
				browser.scripting.executeScript({
			      target : {tabId : tab.id},
			      func : notify,
			      args : [ details.url ],
			    });
		});
    },
    {urls: ['*://*/*master.m3u8*']}
);
