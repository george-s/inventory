$(document).ready(function(){
			$('.my-countdown').countdown({
				until: $.countdown.UTCDate(
					-4, 2017, 3, 1, 0, 0, 0	
				)
			});
		});