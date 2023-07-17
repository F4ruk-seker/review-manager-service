var ChartData = {
	labels : ["January","February","March","April","May",],
	datasets : [
		{
		data : [65,8,90,81,56,],
		backgroundColor :['rgba(52,152,219,1)','rgba(46,204,113,1)','rgba(155,89,182,1)','rgba(241,196,15,1)','rgba(189,195,199,1)',],
		borderColor : ['rgba(136,136,136,0.5)','rgba(170,170,170,1)','rgba(155,89,182,1)','rgba(241,196,15,1)','rgba(189,195,199,1)',],
		label:"2013"},

]
	};
ChartOptions= {
responsive:false,
	layout:{padding:{top:12,left:6,bottom:12,},},
	plugins:{
datalabels:{display:false},
},
legend:{display:false},elements: {
	arc: {borderWidth:0.01,
},
	line: {
},
	rectangle: {
},
},
tooltips:{enabled:false},
hover:{
	mode:'nearest',
	animationDuration:400,
},
};