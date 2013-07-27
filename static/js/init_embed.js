/**
 * DOM initialization script - @author Yane Frenski
 */

  // initiating the scene
  initScene();
  animateScene();
  $('#div-legend').children('h4').html(chartTitle);
  
  if ( chartType == 'pie' ) {
    initLegend($('#div-legend-data'), schema);
  }

