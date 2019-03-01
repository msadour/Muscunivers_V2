$('.input_form_search').keyup(function(){
    var user_search = $(this).val()


    $.ajax({
        url : '/get_users_list_search',
        dataType : 'json',
        data: {
          'user_search': user_search
        },

        success : function(response){
            $(".input_form_search").autocomplete({
                source: response['list_users'],
            });
        },
        error: function(error) {
            console.log('******************')
            console.log(error)
            //alert('error')
        }
    });
})