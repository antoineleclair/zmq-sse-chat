var source = null;

$(function() {
    source = new EventSource('/events');
    source.addEventListener('message', messageReceived, false);
});

function messageReceived(event) {
    $('#time').html(event.data);
}
