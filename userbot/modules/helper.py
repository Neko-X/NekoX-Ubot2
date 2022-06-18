""" Userbot module for other small commands. """
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, man_cmd


@man_cmd(pattern="ihelp$")
async def usit(event):
    me = await event.client.get_me()
    await edit_or_reply(
        event,
        f"**Hai {me.first_name} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        f"× **Group Support :** [𝙽𝚎𝚔𝚘𝚇𝚒𝚍](t.me/)\n"
        f"× **Channel :** [𝙽𝚎𝚔𝚘𝚇𝚒𝚍](t.me/NekoXidch)\n"
        f"× **Owner Repo :** [𝙽𝚎𝚔𝚘𝚇𝚒𝚍](t.me/Nekocannn)\n"
        f"× **Repo :** [𝙽𝚎𝚔𝚘𝚇𝚒𝚍](https://github.com/BTRExo/NekoXid)\n",
    )


@man_cmd(pattern="listvar$")
async def var(event):
    await edit_or_reply(
        event,
        "**Daftar Lengkap Vars Dari 𝙽𝚎𝚔𝚘𝚇𝚒𝚍:** [KLIK DISINI](https://telegra.ph/List-Variabel-Heroku-untuk-Man-Userbot-09-22)",
    )


CMD_HELP.update(
    {
        "helper": f"**Plugin : **`helper`\
        \n\n  •  **Syntax :** `{cmd}ihelp`\
        \n  •  **Function : **Bantuan Untuk 𝙽𝚎𝚔𝚘𝚇𝚒𝚍.\
        \n\n  •  **Syntax :** `{cmd}listvar`\
        \n  •  **Function : **Melihat Daftar Vars.\
        \n\n  •  **Syntax :** `{cmd}repo`\
        \n  •  **Function : **Melihat Repository 𝙽𝚎𝚔𝚘𝚇𝚒𝚍.\
        \n\n  •  **Syntax :** `{cmd}string`\
        \n  •  **Function : **Link untuk mengambil String 𝙽𝚎𝚔𝚘𝚇𝚒𝚍.\
    "
    }
)
