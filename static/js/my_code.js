let csrf_token = $('input[name="csrfmiddlewaretoken"]').val()

$("#product_delete_modal_button").on("click", function (e) {
    e.preventDefault();
    var btn = $(this);
    let data = {
        "id": $('input[name="product_delete_modal_input"]').val(),
    }
    url = btn.attr("data-href-template")
    console.log(url)
    console.log(data)
    execute_delete_product_post_request(url,data)
})

function execute_delete_product_post_request(url, data) {


    $.ajax({
        type: "POST",
        url: url,
        data: data,
        headers: {
            "X-CSRFToken": csrf_token

        },
        success: function (data) {
            $(".close").click()
            // localStorage.setItem("msg", "✅ Расчет успешно удален")
            window.location.reload();


        }

    }) 
}

$("#client_delete_modal_button").on("click", function (e) {
    e.preventDefault();
    var btn = $(this);
    let data = {
        "id": $('input[name="client_delete_modal_input"]').val(),
    }
    url = btn.attr("data-href-template")
   
    execute_delete_client_post_request(url,data)
})

function execute_delete_client_post_request(url, data) {


    $.ajax({
        type: "POST",
        url: url,
        data: data,
        headers: {
            "X-CSRFToken": csrf_token

        },
        success: function (data) {
            $(".close").click()
            // localStorage.setItem("msg", "✅ Расчет успешно удален")
            window.location.reload();


        }

    }) 
}

$(".initial_calculation_book").on("click", function (e) {
    e.preventDefault();
    var btn = $(this);
    var page_amount = document.getElementById('page_amount').value;
    var page_size = document.getElementById('page_size').value;
    var color = document.querySelector("input[type='radio'][name='color']:checked")?.value;
    var cover = document.querySelector("input[type='radio'][name='cover']:checked")?.value;
    var binding = document.querySelector("input[type='radio'][name='binding']:checked")?.value;
    // var paper = document.querySelector("input[type='radio'][name='paper']:checked")?.value;
    let data = {
        "page_amount": page_amount,
        "page_size":page_size,
        "color":color,
        "cover":cover,
        "binding":binding,
        // "paper":paper
    }
   
    url = btn.attr("data-href-template")
    if ( page_amount == '' || color == null || cover==null || binding==null || page_size==0 ){
    }
    else{
        execute_initial_calculation_post_request(url,data)
    }

    
    
})
Number.prototype.toCurrencyString = function(){
    return this.toFixed(2).replace(/(\d)(?=(\d{3})+\b)/g, '$1 ');
}

function execute_initial_calculation_post_request(url, data) {
    Number.prototype.formatMoney = function (decPlaces, thouSeparator, decSeparator) {
        var n = this,
            decPlaces = isNaN(decPlaces = Math.abs(decPlaces)) ? 2 : decPlaces,
            decSeparator = decSeparator == undefined ? "." : decSeparator,
            thouSeparator = thouSeparator == undefined ? "," : thouSeparator,
            sign = n < 0 ? "-" : "",
            i = parseInt(n = Math.abs(+n || 0).toFixed(decPlaces)) + "",
            j = (j = i.length) > 3 ? j % 3 : 0;
        return sign + (j ? i.substr(0, j) + thouSeparator : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + thouSeparator) + (decPlaces ? decSeparator + Math.abs(n - i).toFixed(decPlaces).slice(2) : "");
    };
    console.log(data)

    $.ajax({
        type: "POST",
        url: url,
        data: data,
        headers: {
            "X-CSRFToken": csrf_token

        },
        success: function (data) {
           
            console.log(data.data)
            // $(".close").click()
            // localStorage.setItem("msg", "✅ Расчет успешно удален")
            // window.location.reload();
            $("#initial_price").text(parseFloat(data.data).formatMoney(2, ' ', ',') + " сўм");
  


        }

    }) 
}

