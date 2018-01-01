	
			function ajax_action(result){
			//option
			option = {
						title : {
							text: '开盘价',
							subtext: '纯属虚构'
						},
						tooltip : {
							trigger: 'axis'
						},
						grid: {
					x: 80,
					y: 40,
					x2:20,
					y2:25
				},
						legend: {
							data:['涨幅']
						},
						toolbox: {
							show : true,
							feature : {
								mark : {show: true},
								dataView : {show: true, readOnly: false},
								magicType : {show: true, type: ['line', 'bar']},
								restore : {show: true},
								saveAsImage : {show: true}
							}
						},
						calculable : true,
						xAxis : [
							{
								type : 'category',
								boundaryGap : false,
								data : result.columns
							}
						],
						yAxis : [
							{
								type : 'value',
								
							}
						],
						series : [
							
							{
								name:'涨幅',
								type:'line',
								data:result.data[0],
								
								
							}
						]
					};
										
									
			  
			 
			    var myCharts = echarts.init(document.getElementById("main3"));
				myCharts.setOption(option); 
				
			}
			
			
			var rq = "action=get_change&stock=000002";
			do_ajax(rq);
				
				
				
			//k线图
			function ajax_action_k(result){
				
			//option
			

			option = {
				title : {
					text: '2013年上半年上证指数'
				},
				tooltip : {
					trigger: 'axis',
					showDelay: 0,             // 显示延迟，添加显示延迟可以避免频繁切换，单位ms
					formatter: function (params) {
						var res = params[0].name;
						res += '<br/>' + params[0].seriesName;
						res += '<br/>  开盘 : ' + params[0].value[0] + '  最高 : ' + params[0].value[3];
						res += '<br/>  收盘 : ' + params[0].value[1] + '  最低 : ' + params[0].value[2];
						return res;
					}
				},
				legend: {
					data:['上证指数','成交金额(万)','虚拟数据']
				},
				toolbox: {
					show : true,
					feature : {
						mark : {show: true},
						dataZoom : {show: true},
						magicType : {show: true, type: ['line', 'bar']},
						restore : {show: true},
						saveAsImage : {show: true}
					}
				},
				dataZoom : {
					y: 250,
					show : true,
					realtime: true,
					start : 50,
					end : 100
				},
				grid: {
					x: 80,
					y: 40,
					x2:20,
					y2:25
				},
				xAxis : [
					{
						type : 'category',
						boundaryGap : true,
						axisTick: {onGap:false},
						splitLine: {show:false},
						data : result.index
					}
				],
				yAxis : [
					{
						type : 'value',
						scale:true,
						boundaryGap: [0.05, 0.05],
						splitArea : {show : true}
					}
				],
				series : [
					{
						name:'上证指数',
						type:'k', // 开盘，收盘，最低，最高
						data:result.data
					},
					{
						name:'60日均线',
						type:'line', // 收盘价
						data:result.ma60
					},
					{
						name:'成交金额(万)',
						type:'line',
						symbol: 'none',
						data:[]
					},
					{
						name:'虚拟数据',
						type:'bar',data:[]
					}
					
				]
			};	
			  var myCharts = echarts.init(document.getElementById("main0"));
			  myCharts.setOption(option); 
			
			}
			
			
			function do_ajax_k(rq){
					
					$.ajax({
						type: "post",
						async: true,            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
						url: url+rq,    
						data: {},
						dataType: "jsonp",        //返回数据形式为json
						jsonp:"jsoncallback",
						success:function(result){
								
							if(result){
								
								ajax_action_k(result);
								
						}
						}
				});	
			}
			var rq = "action=get_hist_k&stock=000002";
			do_ajax_k(rq);	
						
                
		
		
	