var source = null;

$(function() {
    source = new EventSource('/events');
    source.addEventListener('message', messageReceived, false);
    $('#shout-box').submit(submitMessage);
});

function messageReceived(event) {
    $('#messages').append('<p>' + JSON.parse(event.data)['message'] + '</p>');
}

function submitMessage() {
    var message = $(this).find('textarea').val();
    $.ajax({
        url: '/push',
        data: JSON.stringify({message: message}),
        type: 'post',
        success: function() {
            console.log('message sent');
        }
    });
    $(this).find('textarea').val('');
    return false;
}
