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
});


$(window).resize(function(e){
    setFooterCls(); 
});
