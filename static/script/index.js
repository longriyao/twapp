 $(function(){

    // 计时器
    var interval = 1000;
    function ShowCountDown(year,month,day,divname) {
        var now = new Date();
        var endDate = new Date(year,month-1, day, now.getHours()+8);
        var leftTime=endDate.getTime()-now.getTime();
        var leftsecond = parseInt(leftTime/1000);
        var day1=Math.floor(leftsecond/(60*60*24));
        var hour=Math.floor((leftsecond-day1*24*60*60)/3600);
        var minute=Math.floor((leftsecond-day1*24*60*60-hour*3600)/60);
        var second=Math.floor(leftsecond-day1*24*60*60-hour*3600-minute*60);
        var cc = document.getElementById(divname);
        cc.innerHTML ="<span id='h'>"+0+hour+"</span>"+"<span class='colon'>時</span>"+"<span id='m'>"+minute+"</span>"+"<span class='colon'>分</span>"+"<span id='s'>"+second+"</span>"+"<span class='colon'>秒</span>";
    }
    window.setInterval(function(){ShowCountDown(2018,4,20,'timer');}, interval)

    // 回到顶部
    $(".m-goToTop").click(function(event) {
        $(window).scrollTop(0);
    });

    // 轮播图
    var h = $(window).height();
    var mySwiper1 = new Swiper('.swiper-container', {
        autoplay: 3000,
        loop: false,
        autoHeight:true,
        pagination: '.swiper-pagination',
        paginationType: 'custom',
        paginationCustomRender: function(swiper, current, total) {
            var text = "";
            for (var i = 1; i <= total; i++) {
                if (current == i) {
                    text += "<span class='redicon'></span>";
                } else {
                    text += "<span class='whiteicon'></span>";
                }
            }
            return text;
        }
    });


    //销售百分比
    function percent(){
        //获取时间点
        var curhour= $('.percentBar').attr('data-value');
        var base=0,range=0;
        var percent   = document.getElementById("percentNum");
        var progress  = document.getElementById("progress");
        var soldNum  = document.getElementById("soldNum");
        if(curhour<=10000){
            base=70;range=5;
        }else
        if(curhour<=20000){
            base=70;range=10;
        }else
        if(curhour<=40000){
            base=70;range=15;
        }else
        if(curhour<=80000){
            base=70;range=20;
        }else
        if(curhour<=130000){
            base=70;range=25;
        }else
        if(curhour<200000){
            base=70;range=28;
        }
        var opercent=Math.floor(range+base);
        progress.style.width = percent.innerHTML = opercent+"%";
    }
    percent();

    // 显示属性层
    $('.btn-addToCart').on('click', function(event) {
        event.preventDefault();
        $('#page-order').show();
        $("#page-index").hide();
        $(window).scrollTop(0);
    });
    $('.detailback').on('click', function(event) {
        event.preventDefault();
        $('#page-order').hide();
        $("#page-index").show();
    });
    $('#val-sel').on('click', function(event) {
        event.preventDefault();
        $('#page-order').show();
        $("#page-index").hide();
        $(window).scrollTop(0);
    });

    
});

