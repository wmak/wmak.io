<head>
	<style>
		body {
			margin: 0;
			overflow: hidden;
		}
		#map-canvas { 
			height: 100%; 
			margin: 0;
			margin-bottom: -42px;
			overflow: auto;
			padding: 0;
		}

		#talon-tag {
			left: -50%;
			width: 400px;
			font-size: 150%;
			text-align: center;
			position: relative;
		}
	</style>
	<title> Talon </title>
	<link rel="icon" type="image/png" href="favicon.png" />
	<script type="text/javascript" src="js/talon.js"></script>
    <script type="text/javascript"
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAd1awIlzqSWUk8mAXj2BhCc6qn_dvjxlM">
	</script>
	<script type="text/javascript">
		function _encode(loc) {
			val = 0
			if (loc < 0) {
				val = 0
				if (loc < -90) {
					val = 1000000000
					loc += 90
				}
			} else {
				val = 2000000000
				if (loc > 90) {
					val = 3000000000
					loc -= 90
				}
			}
			val += Math.abs(loc) * 10000000
			val = parseInt(val)
			val = val.toString(16)
			first = String.fromCharCode(parseInt(val.substring(0, 4), 16))
			second = String.fromCharCode(parseInt(val.substring(4), 16))
			return first + second
		}

		function encode(lat, lon) {
			return "\u2641" +  _encode(lat) + _encode(lon)
		}

		function _decode(loc) {
			first = loc.charCodeAt(0).toString(16) + loc.charCodeAt(1).toString(16)
			val = parseInt(first, 16)
			neg = 1
			if (val < 2000000000) {
				neg = -1
			}
			increase = val.toString().charAt(0) == 1 || val.toString().charAt(0) == 3
			if (val > 1000000000) {
				val = parseInt(val.toString().substring(1))
			}
			val = val / 10000000.0
			if (increase) {
				val += 90
			}
			return val * neg
		}

		function decode(code){
			if (code.charAt(0) != "\u2641") {
				return -1
			}
			lat = _decode(code.substring(1,3))
			lon = _decode(code.substring(3))
			return [lat, lon]
		}
		var initial = window.location.search.substr(1) || "%25E2%2599%2581%25E9%2585%258E%25EE%258F%2599%25E2%25BC%25B3%25E5%25A2%259D"
		initial = decodeURI(decodeURI(decodeURI(decodeURI(escape(encodeURI(initial))))))
		var map
		var marker
		var latlng = new google.maps.LatLng(43.7866457, -79.1894173)
		function current_url() {
			return location.protocol + '//' + location.host + location.pathname
				+ "?"
		}
		function initialize() {
			document.getElementById("talon-tag").value = current_url() + (encode(43.7866457, -79.1894173))
			var mapOptions = {
				center: latlng,
				zoom: 16
			};
			map = new google.maps.Map(document.getElementById('map-canvas'),
				mapOptions);
			marker = new google.maps.Marker({
				position: latlng,
				draggable: true,
				map: map,
				title: "Talon Tag",
				animation: google.maps.Animation.DROP,
			});
			map.setCenter(marker.getPosition());
			google.maps.event.addListener(marker, 'mouseup', function() {
				var position = marker.getPosition()
				map.panTo(position);
				document.getElementById("talon-tag").value = current_url() + (encode(position.k, position.B))
				window.history.pushState("object or string", "Title", "?" +	(encode(position.k, position.B)));
			});
			pos = decode(initial)
			if (pos != -1) {
				pos = new google.maps.LatLng(pos[0], pos[1])
				marker.setPosition(pos)
				map.panTo(pos);
				document.getElementById("talon-tag").value = current_url() + (initial)
			}
		}

		google.maps.event.addDomListener(window, 'load', initialize);
	</script>
	<script>
		(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
			(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new
				Date();a=s.createElement(o),
				m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
		})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

		ga('create', 'UA-54739310-1', 'auto');
		ga('send', 'pageview');
	</script>
</head
<body>
	<div id="map-canvas"></div>	
	<div style="left: 50%; position: absolute;">
		<input type="text" id="talon-tag">
	</div>
</body>
