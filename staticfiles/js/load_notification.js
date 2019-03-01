setInterval(function(){
    // -------------------------- Notification --------------------------
    $.ajax({
       url: '/get_number_new_notifications',
          data: {},
          success: function(data) {
            var current_item = JSON.parse(data)
            if (current_item['nb_notifications'] > 0){
                $('#badge_notification').html(current_item['nb_notifications'])
            }

          }
    });

    // -------------------------- Message --------------------------

    $.ajax({
       url: '/get_number_new_message',
          data: {},
          success: function(data) {
            var current_item = JSON.parse(data)
            if (current_item['num_discussion'] > 0){
                $('#badge_message').html(current_item['num_discussion'])
            }

          }
    });

    // -------------------------- Request contact --------------------------

    $.ajax({
       url: '/get_number_new_request_contact',
          data: {},
          success: function(data) {
            var current_item = JSON.parse(data)
            if (current_item['nb_request_contact'] > 0){
                $('#badge_request_contact').html(current_item['nb_request_contact'])
            }

          }
    });

}, 10000000)