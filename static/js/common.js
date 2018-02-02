/**
 * Created by alexy on 28.05.15.
 */
$(function() {

  var current_url = '/'+location.href.split('/')[3]+'/';
  $('.nav-list-item__link').each(function () {
    if($(this).attr('href') == current_url) $(this).addClass('nav-list-item__link_active');
  });
  $(".input[name='phone']").mask("+7 (999) 999-99-99");
  //$(document).on('click', 'a[href^=#]', function () {
  //    $('html, body').animate({ scrollTop:  $('a[name="'+this.hash.slice(1)+'"]').offset().top }, 300 );
  //    return false;
  //});
  $('.js-select-city').click(function(){
    $('.header-city-select__list').slideToggle();
  });

  // Галлерея фотографий
  $('.js-gallery').fancybox({
    helpers: {
      overlay: {
        locked: false
      }
    }
  });
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
  // Модальное окно открытия формы заявки для главной страницы

  $('.js-main-ticket-button').fancybox({
    helpers: {
      overlay: {
        locked: false
      }
    },
    afterClose: function (e) {
      $('.js-main-ticket-form_modal').trigger('reset');
    }
  });
  $('.js-city-ticket-button').fancybox({
    helpers: {
      overlay: {
        locked: false
      }
    },
    afterClose: function (e) {
      $('.js-city-ticket-form_modal').trigger('reset');
    }
  });
  //$('section').addClass("hidden").viewportChecker({
  //  classToAdd: 'visible animated fadeIn',
  //  offset: 100
  //});
  //$('.section-video-container, .section-advantage-list').addClass("hidden").viewportChecker({
  //  classToAdd: 'visible animated fadeIn',
  //  offset: 200
  //});
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
  //$('#js-form-bp-download a').click(function(){
  //  $.fancybox.close();
  //});
  $.validator.messages.required = "* поле обязательно для заполнения";
  $( "header form" ).validate({
    rules: {
      name: {
        required: true
      },
      phone: {
        required: true
      }
    },
    submitHandler: function(e) {
      $('header form').ajaxSubmit({
          success: function(data){
            if (data.success) {
              $.notify('Ваша заявка принята!', 'success');
            } else {
              $.notify('Что то пошло не так', 'error');
            }
            $('form').trigger('reset');
          }
      });
    }
  });


  $('.section-address-container-item-link').hover(function(){
    $(this).find('.section-address-container-item-link-back').toggle();
  });

  $('.flexslider').flexslider({
    animation: "slide"
  });

  // Модальная форма отправки заявки с главной страницы
  $( ".js-main-ticket-form_modal" ).validate({
    rules: {
      name: {
        required: true
      },
      phone: {
        required: true
      }
    },
    submitHandler: function(e) {
      $('.js-main-ticket-form_modal').ajaxSubmit({
          success: function(data){
            $.fancybox.close();
            if (data.success) {
              $.notify('Ваша заявка принята!', 'success');
            } else {
              $.notify('Что то пошло не так', 'error');
            }
          }
      });
    }
  });
  // Модальная форма отправки заявки со страницы города
  $(".js-city-ticket-form_modal").validate({
    rules: {
      city: {
        required: true
      },
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
      $('.js-city-ticket-form_modal').ajaxSubmit({
          success: function(data){
            $.fancybox.close();
            if (data.success) {
              $.notify('Ваша заявка принята!', 'success');
            } else {
              $.notify('Что то пошло не так', 'error');
            }
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
  // Форма отправки заявки со страницы города
  $( ".js-city-ticket-form" ).validate({
    rules: {
      city: {
        required: true
      },
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
      $('.js-city-ticket-form').ajaxSubmit({
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

  $('.js-slide').fancybox({
    helpers: {
      overlay: {
        locked: false
      }
    }
  });

  $('.js-section-review-slider').flexslider({
    animation: "slide",
    animationLoop: true,
    controlNav: false,
    itemWidth: 250,
    itemMargin: 3,
    prevText: '',
    nextText: ''
  });
  var h_hght = 150;
  var h_mrg = 0;
  $(window).scroll(function(){
    var top = $(this).scrollTop();
    var elem = $('.fixed_menu');
    if (top+h_mrg < h_hght) {
      elem.removeClass('hide');
    } else {
      elem.addClass('hide');
    }
  });

  $('.js-header-franchise-slider').flexslider({
    animation: "fade",
    slideshow: true,
    animationSoeed: 200,
    animationLoop: true,
    pauseOnHover: true,
    controlNav: false,
    itemWidth: 610,
    itemMargin: 3
  });

  var calculator = $('.franchise-calc');
  calculator.find('button').click(function(){
    var ammount = 5000;
    var lift = calculator.find('#lift_count');
    var price = calculator.find('#price');
    var dohod = calculator.find('#dohod');
    var lift_val = lift.val();
    if (lift_val > 10) {
      ammount = 2500
    }
    price.val(lift.val() * ammount);
    dohod.val(lift.val() * ammount);
  });

});