function iniciarMap(){
    var coord = {lat:-33.54970923907112,lng:-70.76762642258622};
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 17,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}