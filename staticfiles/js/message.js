$(function() {
    $('#search_form_chatting').each(function() {
        $(this).find('#input_search_user_chatting').keypress(function(e) {
            // Enter pressed?
            if(e.which == 10 || e.which == 13) {
                $('#search_form_chatting').submit();

            }
        });
    });
});

$('.send_message').click(function(){
    message = $('#message_form').val()
    user = $(this).closest("form").attr('name');

    $.ajax({
        url : '/send_message',
        dataType : 'json',
        data: {
          'message': message,
          'user': user
        },

        success : function(response){
            console.log('Success')
        },
        error: function(error) {
            console.log('******************')
            console.log(error)
        }
    });
})


$('#message_input').each(function(){
    $(this).find('#message_form').keypress(function(e) {

        if(e.which == 13) {
            message = $('#message_form').val()
            $('#message_form').val('')
            user = $(this).closest("form").attr('name');
            $.ajax({
                url : '/send_message',
                dataType : 'json',
                data: {
                  'message': message,
                  'user': user
                },

                success : function(response){
                    console.log('Success')
                },
                error: function(error) {
                    console.log('******************')
                    console.log(error)
                }
            });

        }
    })
})

$('#message_form').keyup( function() {
  $(this).val( $(this).val().replace( /\r?\n/gi, '' ) );
});

setInterval(function(){
    contact = $('#message_input').closest("form").attr('name');

    $.ajax({
       url: '/update_conversation',
          data: {
            'contact': contact
          },
          success: function(data) {
            $('#messages').html(data);
          }
    });
}, 1000)

$('#input_search_user_chatting').keyup(function(){
    var search = $(this).val()

    $.ajax({
        url : '/search_user_chatting',
        dataType : 'json',
        data: {
          'search': search
        },

        success : function(response){
            console.log(response['result'])
            $("#input_search_user_chatting").autocomplete({
                source: response['result'],
            });
        },
        error: function(error) {
            console.log('******************')
            console.log(error)
            //alert('error')
        }
    });
})