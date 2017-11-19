from datetime import timedelta
from typing import Optional  # noqa: F401

from lib.data import ChatCommandArgs
from lib.helper.chat import cooldown, feature, permission


@cooldown(timedelta(seconds=15), 'bingo', 'moderator')
@feature('bingo')
async def commandBingo(args: ChatCommandArgs) -> bool:
    bingoCard: str
    bingoCard = await args.data.getChatProperty(args.chat.channel, 'bingoCard')

    if bingoCard:
        args.chat.send(f'Bingo Card: {bingoCard}')
    elif args.permissions.moderator:
        args.chat.send(
            'No Bingo Card was set. Use !setbingo to set a Bingo Card')
    return True


@feature('bingo')
@permission('moderator')
async def commandSetBingo(args: ChatCommandArgs) -> bool:
    bingoCard: Optional[str] = args.message.query or None
    await args.data.setChatProperty(args.chat.channel, 'bingoCard', bingoCard)
    if bingoCard is None:
        args.chat.send('Bingo Card is now unset')
    else:
        args.chat.send(f'Bingo Card set as {bingoCard}')
    return True
