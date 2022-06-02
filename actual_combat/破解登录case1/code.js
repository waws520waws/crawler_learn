const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);
window = dom.window;
document = window.document;
XMLHttpRequest = window.XMLHttpRequest;


function getparam(username, password) {
	var a = {
            username: username,
            password: password,
            captcha: ""
    };

	return 'qwe'
}
