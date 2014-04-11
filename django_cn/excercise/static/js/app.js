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

    $('table th input').change(function() {
        
        if ($(this).hasClass('checked')) {
            $(this).parents('table').find('td input[type="checkbox"]').removeAttr('checked');
            
        } else {
            $(this).parents('table').find('td input[type="checkbox"]').prop( "checked", true );
            
        }
        $(this).toggleClass('checked');
    });
});


$(window).resize(function(e){
    setFooterCls(); 
});