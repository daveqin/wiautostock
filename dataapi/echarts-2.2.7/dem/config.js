//服务器链接
var url = "http://127.0.0.1:6341/?";


		
//获取链接参数
function GetQueryString(name)
{
     var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
     var r = window.location.search.substr(1).match(reg);
     if(r!=null)return  unescape(r[2]); return null;
}
function ajax_action(result){return 0};

function do_ajax(rq){
				
					$.ajax({
						type: "post",
						async: true,            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
						url: url+rq,    
						data: {},
						dataType: "jsonp",        //返回数据形式为json
						jsonp:"jsoncallback",
						success:function(result){
							if(result){
								ajax_action(result);
								//alert(result);
						}
						}
				});
				
				
			}
	