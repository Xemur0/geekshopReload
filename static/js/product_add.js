window.onload = function (){
    $('.product_add').on('click', 'input[type="button"]',function (){
        let t_href = event.target;
        console.log(t_href.name);
        console.log(t_href.value);
        $.ajax(
            {
                url: '/products/product_add/' + t_href.name + "/" + t_href.value + "/",
                success: function (data) {
                $('.product_add').html(data.result);
            },

            });
        event.preventDefault();


    });
    }