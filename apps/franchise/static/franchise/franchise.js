/**
 * Created by alexy on 17.01.18.
 */
$(function(){
  $('.js-modal-bp-download-btn').fancybox({
    helpers: {
      overlay: {
        locked: false
      }
    },
    afterClose: function (e) {
      $('.bp-download-form').trigger('reset');
      $('#js-form-bp-download').find('input').show();
    }
  });
  $('#js-form-bp-download').validate({
    rules: {
      phone: {
        required: true
      },
      email: {
        required: true,
        email: true
      }
    },
    submitHandler: function(e) {
      $('#js-form-bp-download').ajaxSubmit({
          success: function(data){
            if (data.success) {
              $('#js-form-bp-download').find('input').hide();
              $('#js-form-bp-download').append('<a href="http://elitkadom.ru' + data.file + '" target="_blank" class="button">Скачать файл</a>');
              $('#js-form-bp-download a').click(function(){
                $.fancybox.close();
              });
            } else {
              $.notify('Что то пошло не так', 'error');
            }
            $('#js-form-bp-download').trigger('reset');
          }
      });
    }
  });
  // Форма отправки заявки с главной страницы
  $( ".js-main-ticket-form" ).validate({
    rules: {
      name: {
        required: true
      },
      phone: {
        required: true
      },
      email: {
        required: true,
        email: true
      }
    },
    submitHandler: function(e) {
      $('.js-main-ticket-form').ajaxSubmit({
          success: function(data){
            $.fancybox.close();
            if (data.success) {
              $.notify('Ваша заявка принята!', 'success');
            } else {
              $.notify('Что то пошло не так', 'error');
            }
            $('.js-main-ticket-form').trigger('reset')
          }
      });
    }
  });

  // Галлерея фотографий
  $('.js-gallery').fancybox({
    helpers: {
      overlay: {
        locked: false
      }
    }
  });

});