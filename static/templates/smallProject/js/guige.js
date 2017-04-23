
 $(function(){
    // 初始化选择
    $("#comb .tab").eq(0).addClass('tab-sel').find('input').attr("checked", 'true');
    $('#comb').attr('data-price', $("#comb .tab-sel").attr('data-price'));
    $('[currentprice]').html($("#comb .tab-sel").attr('data-price'));
    // 选择产品
    $("#comb .tab").click(function(event) {
        /* Act on the event */
        $(this).addClass('tab-sel').siblings().removeClass('tab-sel');
        $(this).find('input').attr("checked", 'true');
        $(this).siblings().find('input').attr("checked", false);
        $('#comb').attr('data-price', $(this).attr('data-price'));
        $('[currentprice]').html($(this).attr('data-price'));
        refresh_price();
    });

    $('.u-format.count_atrr').each(function(){
        var obj = $(this).find('.tab');
            obj.eq(0).addClass('tab-sel');
        var id = obj.attr('data-id');
        $(this).attr('data-select', id);
    });

    // 选择事件
    $('.u-format.count_atrr').on('click', '.tab', function(){
        var self = $(this);
        var id = self.attr('data-id');
        self.addClass('tab-sel').siblings().removeClass('tab-sel');
        self.parents('.u-format.count_atrr').attr('data-select', id);
        self.parents('.u-format.count_atrr').find('input').val(id);

        var src = self.attr('data-img');
        if( src ){ $('#attrimg').attr('src', src); }
    });
});


function addnumber(){
    $('#num').val(parseInt($('#num').val())+1);
    var num = $('#num').val();
    var price = num * $('.currentprice').html();
    $('#price').html(price);
    refresh_price(); 
}

function minnumber(){
    if($('#num').val() > 1){
        $('#num').val(parseInt($('#num').val())-1);
        var num = $('#num').val();
        var price = num * $('.currentprice').html();
        $('#price').html(price);
        refresh_price();
    }
}

function inputnumber(){
    var number=parseInt($('#num').val());
    if(isNaN(number)||number < 1){
        $('#num').val('1');
        refresh_price();
    }else if(number > 1){
        $('#num').val(number);
    }
    refresh_price();
}

// 刷新价格
function refresh_price() {
    $.ajax({
        url: '/checkout.php?',
        type: 'post',
        data: $('#comb input[checked=checked], #act, input[name=\'num\']'),
        dataType: 'json',
        success: function(json) {
           if(json.ret)
           {
                $("#price").html(json.total);
              $("input[name='price']").val(json.total);
           }
           else{
               alert(json.msg)
           }
        },
        error: function(xhr, ajaxOptions, thrownError) {
        }
    });
}

// 提交表单
function postcheckGuige() {
    $("#form").submit();
    return false;
}