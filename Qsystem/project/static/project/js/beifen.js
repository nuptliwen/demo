$(document).ready(function(){

    $("input.inputfield").focus(function(){
      $(this).attr("value","");
    });

    $("input.inputfield").blur(function(){
      if($(this).attr("value") == ""){
        $(this).attr("value","请输入1-1000的数字");
      }
      
    });
    
    $("#filepath input").focus(function(){
      $(this).attr("value","");
    });

    $("#filepath input").blur(function(){
      if($(this).attr("value") == ""){
        $(this).attr("value","请输入文件路径");
      }
      
    });

    $("#test").click(function(){
      var testerlist = $("#testerlist input");
    	var jsontester = { tester:[]};
      if(testerlist.length == 0){
	      console.log('no data');
     	}
	    for (var i = testerlist.length - 1; i >= 0; i--) {
	      var item = testerlist.eq(i);
	      if(item.attr("checked") === "checked"){
		      var temp = {value:item.attr("id"), name:item.parent().text()};
		      jsontester.tester.push(temp);
	      }
	      //console.log(jsontester);
	    }
        $("[title='1']").children("div").remove();
        for (var i= jsontester.tester.length-1; i >=0; i--){
            $("[title='1']").append('<div class="role-item" value=">' + jsontester.tester[i].value+'" type="radio"><span>'+jsontester.tester[i].name+'</span><span class="close">x</span></div>');
        }	

        pl = $("[title='1']").children("div").length;
        console.log(pl);
        if(pl >= 8){
          w = (pl/5+1)*30;
          $("[title='1']").attr("style","height:"+w+"px;");
        }
        $("[title='1']").attr("title","0");

    });

    $(".role-item .close").live('click',function(){
        $(this).parent().remove();
    });

    $(".roles .btn-success").click(function(){      
      $("#select").modal("show");
      $(this).next().attr("title","1");
    });

//选择项目负责人
    $("#master").focus(function(){
      p = $(".role-item");  
      //console.log(p);
      $("#master").children("option").remove();
      for(var i=p.length-1; i >=0; i--){
        item = p.eq(i);
        $("#master").append("<option>"+item.children('span').eq(0).text()+"</option>");
        //console.log(item.children('span').eq(0).text());
      } 
    });

    //计算天数
    $(".range input").change(function(){
        var endtime = $(this).val().split("-", 3);
        var s = $(this).parent().prev("span").prev("span");
        if(s.length > 0){
          var startime = s.eq(0).children('input').val().split("-", 3);
          var stime = Date.UTC(startime[0], startime[1], startime[2]);
          var etime = Date.UTC(endtime[0], endtime[1], endtime[2]);
          var diff = etime - stime; 
          var days = diff/1000/60/60/24 + 1;
          $(this).parent().siblings('div').children('span').text(days);
        }
    });

});
