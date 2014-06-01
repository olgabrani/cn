setFooterCls = function(){
    var WindowHeight = $(window).height();
    var header = $('header').outerHeight();
    var main = $('.main').outerHeight();
    var footer = $('footer').outerHeight();
    var h1= WindowHeight - (header+main+footer);
    h1>0 ? $('footer').addClass('fix'): $('footer').removeClass('fix');
};

$(document).foundation();

$(document).ready(function(){
    setFooterCls();

    if ($('.sortable').length>0) {
        $('.sortable').dataTable({
            bFilter: false,
            bPaginate: false,
            bInfo: false,
        });
        
    }

    if ($('.grade-div').length>0){
        $('.grade-div').find('input[type="text"]').focus();
    }

    $('.toggle-qa').click(function(e){
        e.preventDefault();
        $('.qa-desc').toggle();
        $('.theory').toggle();
    });
    $('.toggle-suggested').click(function(e){
        e.preventDefault();
        $('.suggested-answer').toggle();
    });

    checkForm = function(check) {
        console.log('checkform');
        var val = check.val();
        var el = $("input[name="+val+"]");
        if (check.is(":checked")){
            el.val('checked');
        } else {
            el.val('False');
        }

   }


    $('table th input').change(function() {
        
        if ($(this).hasClass('checked')) {
            console.log('check', check);
            var check = $(this).parents('table').find('td :checkbox');
            check.removeAttr('checked');
            check.each(function(i){
                checkForm($(this));
            });
        } else {
            var check = $(this).parents('table').find('td :checkbox');
            console.log('check', check);
            check.prop( "checked", true );
            check.each(function(i){
                checkForm($(this));
            });
        }
        $(this).toggleClass('checked');
    });
   

    $('.check-fun td').find(':checkbox').bind('change', function(){
        checkForm($(this));
    });

    $('.reveal-modal .cancel').click(function(e){
        e.preventDefault();
        $(this).parents('.reveal-modal').foundation('reveal', 'close');
    });

    $('#reveal-unanswered').click(function(e){
        e.preventDefault();
        $('#unanswered').foundation('reveal','open');
        var cnt = 0;
        $('#exercise-submit').find('textarea').each(function(){
           if( this.value == ''){
                cnt++;
            }
        }); 
        if (cnt > 0 ){
            var text = 'Δεν έχετε απαντήσει σε <strong>'+cnt+'</strong> ερωτήσεις.'
            $('#unanswered .lead span').html(text);
        }

    });

    $('#unanswered .success').click(function(e){
        e.preventDefault();
        $('#exercise-submit').submit();
        console.log('after submit');
        $(this).parents('.reveal-modal').foundation('reveal', 'close');
    });

    $('.qa textarea').bind("paste",function(e) {
        e.preventDefault();
    });
    $('.delete-img').click(function(){
        var question_id = $(this).attr('data-question');
        var user_id = $(this).attr('data-user');
        var send_data = {
            'question_id': question_id,
        };
        var that = $(this);
        $.ajax({
            type: "POST",
            url: "/excercise/delete_image/",
            data: send_data,
        }).done(function( msg ) {
            console.log(msg);
            that.siblings('img').remove();
            that.remove();
        });

    });

    $('.answer .star').click(function(e){
        e.preventDefault();
        var question_id = $(this).attr('data-question');
        var text = $(this).siblings('div').html();
        var send_data = {
            'question_id': question_id,
            'text': text,
        };
        var that = $(this);
        $.ajax({
            type: "POST",
            url: "/excercise/set_suggested_answer/",
            data: send_data,
        }).done(function( msg ) {
            if (msg) {
                that.addClass('selected')
            }
        });

    });
});


$(window).resize(function(e){
    setFooterCls(); 
});
