// 第 1 课：浏览器下载这个文件后，从上到下执行。
// console.log 把内容输出到浏览器开发者工具的 Console 中。
console.log("你好，JavaScript！");
console.log(110);

// 页面演示：找到 id 为 js-message 的段落，再改变它的文字。
// 这两行属于后面要学的 DOM，现在先观察效果即可。
const message = document.querySelector("#js-message");
message.textContent = "JavaScript 已运行：这句话是 learn.js 改出来的。";
