let heart = $('.header svg')
console.log(heart)

function sendrequest(){
    $.ajax({
        url: "/likes_movies/${film_id}",
        data: "GET",
        dataType: "html",
        success: function (data) {
            console.log(data)
            $(heart).toggleClass('liked')
        }
    });
}

$(heart).click(function (e) { 
    e.preventDefault();
    $(this).toggleClass('liked');
});