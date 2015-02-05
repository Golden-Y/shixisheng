$(document).ready(function(){

	$('#toggle-switcher').click(function(){
		if($(this).hasClass('opened')){
			$(this).removeClass('opened');
			$('#style-switcher').animate({'right':'-222px'});
		}else{
			$(this).addClass('opened');
			$('#style-switcher').animate({'right':'-10px'});
		}
	});
	
	$('#style-switcher li').click(function(e){
		e.preventDefault();
		
		$elem = $(this);
		console.log("ssdd");
		$('link#theme').attr('href', 'static/css/shapes/color/shapes-'+$elem.attr('id')+'.css');
		
		$('link#theme').load(function(){
			$('link#main').attr('href', 'static/css/shapes/color/shapes-'+$elem.attr('id')+'.css');
		});
	});
	
	$('#style-switcher .toggle-overlay').click(function(e){
		e.preventDefault();
		
		if($(this).hasClass('off')){
			$(this).removeClass('off').html('ON');
			$('#color-overlay').show();
			$('body').removeClass('no-overlay');
		}
		else{
			$(this).addClass('off').html('OFF');
			$('#color-overlay').hide();
			$('body').addClass('no-overlay');
		}
	});
});