ymaps.ready(function () {
  var myMap;
  var url = $('#map').data('url');
  city = 'Екатеринбург';
  var coord = '';
  var myGeocoder = ymaps.geocode(city);
  myGeocoder.then(
    function (res) {
      coord = res.geoObjects.get(0).geometry.getCoordinates();
      myMap = new ymaps.Map("map", {
        center: coord,
        zoom: 3
      });
      $.ajax({
        url: url
      }).done(function (data) {
        console.log('done');
        if (data.city_list.length) {
          console.log('has');
          var city_list = data.city_list;
          for(var i = 0, len = city_list.length; i < len; i++) {
            myMap.geoObjects.add(
              new ymaps.Placemark([city_list[i]['coord_x'], city_list[i]['coord_y']], {
              balloonContent: city_list[i]['name'] + ' Количество адресов: ' + city_list[i]['house_count'],
              hintContent: city_list[i]['name'] + ' Количество адресов: ' + city_list[i]['house_count']
              })
            );
          }
        } else {
          console.log('Not');
        }
      });
    }
  );
});