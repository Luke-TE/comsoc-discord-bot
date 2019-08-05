const Discord = require('discord.js');
const bot = new Discord.Client();

bot.on('ready', () => {
 console.log(`Logged in as ${bot.user.tag}!`);
 });

bot.on('message', msg => {
 	if (msg.content === 'ping') {
 		msg.reply('pong');
 	}
	if (msg.content === 'communism') {
		msg.reply('https://www.youtube.com/watch?v=U06jlgpMtQs');
	}
	if (msg.content === 'capitalism' || msg.content === 'capitali$m') {
		const member = msg.guild.member(msg.author);
		member.kick().then(() => {
		msg.reply('Capitalist scum aren\'t welcome here >:(')}).catch(e => {
			msg.reply('Nope')
		});
	}
 });

bot.on('guildMemberAdd', member => {
    // Set the member's roles by id
    member.setRoles(['597869786726137887']).then(
    
    ).catch(err => {
    console.log('This aint working bro')
    });
});

bot.login('NTk5NjY5NDYxNzk1OTk1NjYx.XSrxdQ.B7TWRgjOVjeJ4P8Mio7TqYpAaOU');
