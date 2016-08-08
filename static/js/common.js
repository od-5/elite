/**
 * Created by alexy on 28.05.15.
 */
$(function() {

  var current_url = '/'+location.href.split('/')[3]+'/'
  $('.nav-list-item__link').each(function () {
    if($(this).attr('href') == current_url) $(this).addClass('nav-list-item__link_active');
  });

  //$(document).on('click', 'a[href^=#]', function () {
  //    $('html, body').animate({ scrollTop:  $('a[name="'+this.hash.slice(1)+'"]').offset().top }, 300 );
  //    return false;
  //});
  $('.js-select-city').click(function(){
    $('.header-city-select__list').slideToggle();
  });

  // Галлерея фотографий
  $('.js-gallery').fancybox();
  // Модальное окно открытия формы заявки для главной страницы

  $('.js-main-ticket-button').fancybox({
    afterClose: function (e) {
      $('.js-main-ticket-form_modal').trigger('reset');
    }
  });
  $('.js-city-ticket-button').fancybox({
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

  $('.js-slide').fancybox();

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
});