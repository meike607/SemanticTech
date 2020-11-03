#!/usr/bin/perl

use strict;
use warnings;
use RiveScript;

# Create a new RiveScript interpreter object.
my $rs = RiveScript->new();

# Load a directory full of RiveScript documents.
$rs->loadDirectory("./replies");

# You must sort the replies before trying to fetch any!
$rs->sortReplies();

# Enter a loop to let the user chat with the bot using standard I/O.
while (1) {
  print "You> ";
  chomp(my $message = <STDIN>);

  # Let the user type "/quit" to quit.
  if ($message eq "/quit") {
    exit(0);
  }

  # Fetch a reply from the bot.
  my $reply = $rs->reply("user", $message);
  print "Bot> $reply\n";
}

