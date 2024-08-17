const { SlashCommandBuilder } = require("discord.js");

module.exports = {
  data: new SlashCommandBuilder()
    .setName("help")
    .setDescription("How to use the bot!"),
  async execute(interaction) {
    await interaction.reply("I'll replace this later - Juniper, 2024");
  },
};
