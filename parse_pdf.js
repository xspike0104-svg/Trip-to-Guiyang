const { PDFParse } = require('pdf-parse');
const fs = require('fs');

const pdfPath = 'C:\\Users\\pc\\.openclaw\\workspace\\indonesia_law.pdf';
const dataBuffer = fs.readFileSync(pdfPath);

const parser = new PDFParse();
parser.parse(dataBuffer).then(data => {
  console.log('=== PDF 文本内容 ===');
  console.log('页数:', data.numpages);
  console.log('内容长度:', data.text.length, '字符');
  console.log('\n=== 全部文本 ===');
  console.log(data.text);
}).catch(err => {
  console.error('解析失败:', err);
});
