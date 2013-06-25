$(document).ready(function(){
	SyntaxHighlighter.autoloader(
  		'bash shell             /js/syntax_highlighter/scripts/shBrushBash.js',
  		'css                    /js/syntax_highlighter/scripts/shBrushCss.js',
  		'js jscript javascript  /js/syntax_highlighter/scripts/shBrushJScript.js',
  		'py python              /js/syntax_highlighter/scripts/shBrushPython.js',
  		'sql                    /js/syntax_highlighter/scripts/shBrushSql.js'
	);
	
	SyntaxHighlighter.all()	
});