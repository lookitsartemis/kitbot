const { SlashCommandBuilder, EmbedBuilder } = require("discord.js");
const topics = require("../../JSON/topics.json");

module.exports = {
  data: new SlashCommandBuilder()
    .setName("topic")
    .setDescription("Get a random topic."),
  async execute(interaction) {
    const randomIndex = Math.floor(Math.random() * topics.topics.length);
    const randomTopic = topics.topics[randomIndex];

    await interaction.reply(`Question: *${randomTopic}*`);
  },
};
