$(document).ready(function() {
  prettyPrint();

  $('#people li img, article img').hover(
    function() {
      this.tip = this.title;
      $(this).after('<div class="tooltip-box">'+this.tip+'</div>');
      this.title = "";
    },
    function() {
      $('.tooltip-box').remove();
      this.title = this.tip;
    }
  );
});
