$(document).ready(function(){

	var swiper = new Swiper('.swiper-container', {
		loop : true,
		pagination: '.swiper-pagination',
		nextButton: '.swiper-button-next',
		prevButton: '.swiper-button-prev',
		slidesPerView: 'auto',
		autoplay: 5000
	});

	// 顶部轮播
	jQuery(".h-scroll-box").slide({mainCell:".bd ul",autoPlay:true,effect:"leftMarquee",vis:2,interTime:50});

	// 中间轮播
	jQuery(".txtMarquee-top").slide({mainCell:".bd ul",autoPlay:true,effect:"topMarquee",vis:5,interTime:50});

	// 颜色选择
	$(".q-radius-color span").click(function (){
		var selectColor = $(".r-show").html();
		var imgSrc = $(this).attr('src');
		var imgColor = $(this).html();
		$(this).addClass("r-show").siblings().removeClass('r-show');
		$(".changeImg").attr('src', imgSrc);
		// $(".colorObt").html(selectColor);
		
	})

	// 尺寸选择
	$(".q-size-color span").click(function (){
		$(this).addClass("s-show").siblings().removeClass('s-show');
	})


	// 产品数量-1 & +1
	var numChange = $(".q-num").html();
	$(".minus").click(function (){
		if (numChange == 1) {
			numChange == 1
		} else {
			numChange --
			$(".q-num").html(numChange);
			$(".footer span, .moneyObt").html(numChange * 1288);
			// $(".numObt").html(numChange);
		}
	})
	$(".add").click(function (){
		numChange ++
		$(".q-num").html(numChange);
		$(".footer span, .moneyObt").html(numChange * 1288);
		// $(".numObt").html(numChange);
	})

	// 留言聚焦清空
	$("textarea").focus(function (){
		$(this).html('')
	})
	
	// 第一步
	$(".footer").on("click",".firstSteps", function(){
		selection();
	});

	$(".standard").click(function (){
		selection();
	});

	function selection() {
		$(".first-wrap").fadeOut();
		setTimeout(function () {
			$(".quantity").fadeIn();
			$(".firstSteps").addClass("secondSteps").removeClass("firstSteps");
		}, 500);
	}
	

	// 第二步
	$(".footer").on("click",".secondSteps", function(){
		var selectColor = $(".r-show").html();
		var selectSize= $(".s-show").html();
		var qNum = $(".q-num").html();

		console.log(selectColor+selectSize+qNum);
		// ajax下单数据发送后台
		// 第一次ajax提交颜色+型号+数量
		$.ajax({
			url: './projectapp/babyid/1121/',
			type: 'post',
			dataType: 'json',
			data: 'selectColor=' + selectColor + '&selectSize=' + selectSize + '&qNum=' + qNum,
			success: function(data) {
				if (data.msg == 0) {
					// 成功则跳转到froms.html页面
					window.location.href = "froms.html"
				} else {
					// 失败则刷新
					window.location.reload();
				}
			}
		})
	})

	// 第三步 购买表单验证
	$(".footer").on("click",".get", function(){
		var colorObt = $(".colorObt").html();
		var moneyObt = $(".moneyObt").html();
		var numObt = $(".numObt").html();
		var name = $(".name").val();
		var mobile = $(".mobile").val();
		var mailbox = $(".mailbox").val();
		var address = $(".address").val();
		var textarea = $("textarea").val();
			if (name == "") {
				setTimeout(function () {
					alert("姓名不能为空");
				  }, 500);
				return
			}
			if (mobile == "") {
				alert("手机号码不能为空");
				return
			}
			if (mailbox == "") {
				alert("邮箱不能为空");
				return
			}
			if (address == "") {
				alert("详细地址不能为空");
				return
			}
			if (name !== "" && mobile !== "" && mailbox !== "" && address !== "") {
				
				// 测试
				console.log("颜色：" + colorObt);
				console.log("价格：" + moneyObt);
				console.log("数量：" + numObt);
				console.log("手机号码：" + mobile);
				console.log("邮箱：" + mailbox);
				console.log("详细地址：" + address);
				console.log("textarea:" + textarea);

				// ajax下单数据发送后台
				// 第二次ajax提交颜色+型号+数量+姓名+手机号+邮箱+详细地址+留言
				$.ajax({
					url: 'xxxx',
					type: 'post',
					dataType: 'json',
					data: 'colorObt=' + colorObt + '&numObt=' + numObt + '&moneyObt=' + moneyObt + '&name=' + name + '&mobile=' + mobile + '&mailbox=' + mailbox + '&address=' + address + '&textarea=' + textarea,
					success: function(data) {
						if (data.msg == 0) {
							alert('下单成功!');
						} else {
							alert('下单失败，请重试!');
						}
					}
				})

			}
	})

	$(".quantity h2").click(function (){
		window.location.reload();
	})

	$(".receipt h2").click(function (){
		window.location.href = "index.html"
	})

});