CREATE TABLE `start` (
  `id` int(11) NOT NULL,
  `начало` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `start` (`id`, `начало`) VALUES
(1, 'герои '),
(2, 'предметы'),
(3, 'справочник'),
(4, 'пикер');

CREATE TABLE `simple items` (
  `id` int(11) NOT NULL,
  `простые предметы` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `simple items` (`id`, `простые предметы`) VALUES
(1, 'Town Portal Scroll'),
(2, 'Ironwood Branch'),
(3, 'Quelling Blade'),
(4, 'Ring of Regen'),
(5, 'Ring of Health'),
(6, 'Aegis of the Immortal'),
(7, 'Potion'),
(8, 'Gautlets of Strenght'),
(9, 'Ring of protection'),
(10, 'Sages Mask');

CREATE TABLE `neutral items` (
  `id` int(11) NOT NULL,
  `нейтральные предметы` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `neutral items` (`id`, `нейтральные предметы`) VALUES
(1, 'Разряд 1'),
(2, 'Разряд 2'),
(3, 'Разряд 3'),
(4, 'Разряд 4'),
(5, 'Разряд 5');


CREATE TABLE `items` (
  `id` int(11) NOT NULL,
  `предметы` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `items` (`id`, `предметы`) VALUES
(1, 'простые'),
(2, 'сборные'),
(3, 'нейтральные');

CREATE TABLE `heroes` (
  `id` int(11) NOT NULL,
  `герои` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `heroes` (`id`, `герои`) VALUES
(1, 'сила'),
(2, 'ловкость'),
(3, 'интелект');

CREATE TABLE `discharge5` (
  `id` int(11) NOT NULL,
  `разряд5` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `discharge5` (`id`, `разряд5`) VALUES
(1, 'Force Boots'),
(2, 'Stygian Desolator'),
(3, 'Seer Stone'),
(4, 'Mirror Shield'),
(5, 'Apex'),
(6, 'Ballista'),
(7, 'Book of the dead'),
(8, 'Fallen Sky'),
(9, 'Pirat Hat'),
(10, 'Ex Machina'),
(11, 'Giants Ring'),
(12, 'Book of Shadows');

CREATE TABLE `discharge4` (
  `id` int(11) NOT NULL,
  `разряд4` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `discharge4` (`id`, `разряд4`) VALUES
(1, 'Timeless Relic'),
(2, 'Spell Prism'),
(3, 'Flicker'),
(4, 'Ninja Gear'),
(5, 'Illusion Cape'),
(6, 'The Leveller'),
(7, 'Minotaur Horn'),
(8, 'Telescope'),
(9, 'Trickster Cloak'),
(10, 'Stormcrafter'),
(11, 'Penta Edged Sword');

CREATE TABLE `discharge3` (
  `id` int(11) NOT NULL,
  `разряд3` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `discharge3` (`id`, `разряд3`) VALUES
(1, 'Quickening Charm'),
(2, 'Spider Legs'),
(3, 'Paladin Sword'),
(4, 'Orb of Destruction'),
(5, 'Titan Sliver'),
(6, 'Mind Breaker'),
(7, 'Enchanted Quiver'),
(8, 'Elven Tunic'),
(9, 'Cloak of Flames'),
(10, ''),
(11, 'Psychic Headband');

CREATE TABLE `discharge2` (
  `id` int(11) NOT NULL,
  `разряд2` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `discharge2` (`id`, `разряд2`) VALUES
(1, 'Ring of Aquila'),
(2, 'Imp Claw'),
(3, 'Nether Shawl'),
(4, 'Dragon Scale'),
(5, 'Pupls Gift'),
(6, 'Vambrace'),
(7, 'Grove Bow'),
(8, 'Philosopher stone'),
(9, 'Essence Ring'),
(10, 'Bullwhip'),
(11, 'Quicksilver Amulet');

CREATE TABLE `discharge1` (
  `id` int(11) NOT NULL,
  `разряд1` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `discharge1` (`id`, `разряд1`) VALUES
(1, 'Keen Optic'),
(2, 'Ironwood Tree'),
(3, 'Ocean Hert'),
(4, 'Broom Handle'),
(5, 'Trusty Shovel'),
(6, 'Faded Broach'),
(7, 'Arcan Ring'),
(8, 'Royal Jelly'),
(9, 'Chipped Vest'),
(10, 'Possessed Mask'),
(11, 'Fairys Trinket');

CREATE TABLE `directory` (
  `id` int(11) NOT NULL,
  `справочник` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `directory` (`id`, `справочник`) VALUES
(1, 'мета'),
(2, 'роли героев '),
(3, 'словарь '),
(4, 'советы'),
(5, 'моды и команды'),
(6, 'нейтральные крипы'),
(7, 'руны '),
(8, 'вардинг'),
(9, 'фарм');

CREATE TABLE `collect items` (
  `id` int(11) NOT NULL,
  `сборные предметы` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `collect items` (`id`, `сборные предметы`) VALUES
(1, 'Magic Wand'),
(2, 'Buckler'),
(3, 'Veil of Discord'),
(4, 'Hood of Defiance'),
(5, 'Crystalys'),
(6, 'Dragon Lance'),
(7, 'Null Talisman'),
(8, 'Ring of Basilius'),
(9, 'Glimmer Cape'),
(10, 'Vanguard');

CREATE TABLE `agility heroes` (
  `id` int(11) NOT NULL,
  `ловкость герои` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `agility heroes` (`id`, `ловкость герои`) VALUES
(1, 'Anti-mage'),
(2, 'Drow Ranger'),
(3, 'Juggernaut'),
(4, 'Mirana'),
(5, 'Morphling'),
(6, 'Phantom Lancer'),
(7, 'Vengeful Spirit'),
(8, 'Riki'),
(9, 'Sniper'),
(10, 'Templar Assassin'),
(11, 'Luna'),
(12, 'Bouty Hunter'),
(13, 'Ursa'),
(14, 'Gyrocopter'),
(15, 'Lone Druid'),
(16, 'Naga Siren'),
(17, 'Troll Warlord'),
(18, 'Ember Spirit'),
(19, 'Monkey King'),
(20, 'Pangolier'),
(21, 'Hoodwink'),
(22, 'Bloodseeker'),
(23, 'Shadow Fiend'),
(24, 'Razor'),
(25, 'Venomancer'),
(26, 'Faceless Void'),
(27, 'Phantom Assassin'),
(28, 'Viper'),
(29, 'Clinkz'),
(30, 'Broodmother'),
(31, 'Weaver'),
(32, 'Spetre'),
(33, 'Meepo'),
(34, 'Nyx Assassin'),
(35, 'Slark'),
(36, 'Medusa'),
(37, 'Terrorblade'),
(38, 'Arc Warden');

CREATE TABLE `intelligence heroes` (
  `id` int(11) NOT NULL,
  `интеллект герои` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `intelligence heroes` (`id`, `интеллект герои`) VALUES
(1, 'Cristal Maiden'),
(2, 'Puck'),
(3, 'Storm Spirit'),
(4, 'Windranger'),
(5, 'Zeus'),
(6, 'Lina'),
(7, 'Shadow Shaman'),
(8, 'Tinker'),
(9, 'Natures Prophet'),
(10, 'Enchantress'),
(11, 'Jakiro'),
(12, 'Chen'),
(13, 'Silencer'),
(14, 'Ogre Magi'),
(15, 'Rubick'),
(16, 'Disruptor'),
(17, 'Keeper of the light'),
(18, 'Skywrath Mage'),
(19, 'Oracle'),
(20, 'Techies'),
(21, 'Dark Willow'),
(22, 'Void Spirit'),
(23, 'Bane'),
(24, 'Lich'),
(25, 'Lion'),
(26, 'Witch Doctor'),
(27, 'Enigma'),
(28, 'Necrophos'),
(29, 'Warlock'),
(30, 'Queen of Pain'),
(31, 'Death Prophet'),
(32, 'Pugna'),
(33, 'Dazzle'),
(34, 'Leshrac'),
(35, 'Dark Seer'),
(36, 'Batrider'),
(37, 'Ancien Apparition'),
(38, 'Invoker'),
(39, 'Outworld Destroyer'),
(40, 'Shadow Demon'),
(41, 'Visage'),
(42, 'Winter Wyvern'),
(43, 'Grimstroke');

CREATE TABLE `power heroes` (
  `id` int(11) NOT NULL,
  `герои сила` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `power heroes` (`id`, `герои сила`) VALUES
(1, 'Earthshaker'),
(2, 'Sven'),
(3, 'Tiny'),
(4, 'Kunkka'),
(5, 'Beastmaster'),
(6, 'Dragon Knight'),
(7, 'Clockwerk'),
(8, 'Omniknight'),
(9, 'Huskar'),
(10, 'Alchemist'),
(11, 'Brewmaster'),
(12, 'Trent Protector'),
(13, 'Io'),
(14, 'Centaur Warrunner'),
(15, 'Timbersaw'),
(16, 'Bristleback'),
(17, 'Tusk'),
(18, 'Elder Titan'),
(19, 'Legion Commander'),
(20, 'Earth Spirit'),
(21, 'Phoenix'),
(22, 'Mars'),
(23, 'Snapfire'),
(24, 'Axe'),
(25, 'Pudge'),
(26, 'Sand King'),
(27, 'Slardar'),
(28, 'Tidehunter'),
(29, 'Wraith King'),
(30, 'Lifestealer'),
(31, 'Night Stalker'),
(32, 'Doom'),
(33, 'Spirit Breaker'),
(34, 'Lycan'),
(35, 'Chaos Knight'),
(36, 'Undying'),
(37, 'Magnus'),
(38, 'Abaddon'),
(39, 'Underlord');

