$(function () {
    $('#shop_img_small>li').mouseover(function () {
        let index = $(this).index();
        for (let i = 0; i < $('#shop_img_middle>li').length; i++) {
            {
                // #表示被选中
            }
            if (index === i) {
                $('#shop_img_middle>li')[i].style.setProperty('display', 'block')
            } else {
                $('#shop_img_middle>li')[i].style.setProperty('display', 'none');
                {
                    // #  其他的要隐藏
                }
            }
        }

    })

});

const ADD_URL = 'http://127.0.0.1:8000/shopcar/addcar/'

$(function () {
    $('#buy').click(function () {
        let number = $('#number').val();
        let shop_id = $(this).attr('shopid');
        data = {
            number: number,
            shop_id: shop_id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        };

        $.post(ADD_URL , data, function (result) {
                if (result && result.status === 200) {
                    let number = parseInt($('#car_number').text());
                    number += result.content.result.data;
                    $('#car_number').text(number)
                }
                else if (result.status === 302) {
                    window.location.href = result.content
                }
            }
        )
    });
});