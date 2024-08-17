const fs = require("fs");
const path = require("path");
const axios = require("axios");
const { SlashCommandBuilder, EmbedBuilder } = require("discord.js");

module.exports = {
  data: new SlashCommandBuilder()
    .setName("fox")
    .setDescription("Sends a random fox image."),
  async execute(interaction) {
    try {
      const response = await axios.get("https://randomfox.ca/floof/");

      const foxImageUrl = response.data.image;

      const catEmbed = new EmbedBuilder()
        .setColor(0xef976b)
        .setTitle("Fox!")
        .setImage(foxImageUrl);

      await interaction.reply({ embeds: [catEmbed] });
    } catch (error) {
      console.error(error);
      await interaction.reply({
        content: "Failed to fetch a fox image :(",
        ephemeral: true,
      });
    }
  },
};
