
tile_size = 64


class Level_data:
    def __init__(self) -> None:
        self.level_0 = ["                                             ",
                        "      RPPPPPPPPPPPZPPPPPPPPPPPPPPPPS         ",
                        "      NABBBBBBBBBBWBBBBBBBBBBBBBBBCM         ",
                        "      NDEEEEEEEEEEXEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEEEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEEEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEVEEEEEEEEEEEEEEEFM         ",
                        "      NGHHHHHHHHHHWHHHHHHHHVHHHHHHIM         ",
                        "      TKKKKKKKKKKKYKKKKKKKKYKKKKKKKU         ",
                        "                                             ", ]

        self.level_1 = ["                                             ",
                        "      RPPPPPPPPPPPPPPPPPPPPPPPPPPPPS         ",
                        "      NABBBBBBBBBBBBBBBBBBBBBBBBBBCM         ",
                        "      NDEEEEEEEEEEEEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEEEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEEEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEEEEEEEEEEEEEEEEEFM         ",
                        "      NGHHHHHHHHHHHHHHHHHHHHHHHHHHIM         ",
                        "      TKKKKKKKKKKKKKKKKKKKKKKKKKKKKU         ",
                        "                                             ", ]

        self.level_2 = ["                                             ",
                        "      RPPPPPPPPPPPPPPPPPPPPPPPPPPPPS         ",
                        "      NABBBBBBBBBBBBBBBBBBBBBBBBBBCM         ",
                        "      NDEEEEEEEEEEEEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEEEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEEEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEEEEEEEEEEEEEEEEEFM         ",
                        "      NGHHHHHHHHHHHHHHHHHHHHHHHHHHIM         ",
                        "      TKKKKKKKKKKKKKKKKKKKKKKKKKKKKU         ",
                        "                                             ", ]

        self.level_3 = ["                                             ",
                        "      RPPPPPPPPPPPZPPPPPPPPPPPPPPPPS         ",
                        "      NABBBBBBBBBBWBBBBBBBBBBBBBBBCM         ",
                        "      NDEEEEEEEEEEWEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEXEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEEEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEVEEEEEEEEEEEEEEEFM         ",
                        "      NGHHHHHHHHHHWHHHHHHHHHHHHHHHIM         ",
                        "      TKKKKKKKKKKKYKKKKKKKKKKKKKKKKU         ",
                        "                                             ", ]

        self.level_4 = ["                                             ",
                        "      RPPPPPPPPPPPZPPPPPPPPPPPPPPPPS         ",
                        "      NABBBBBBBBBBWBBBBBBBBBBBBBBBCM         ",
                        "      NDEEEEEEEEEEWEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEXEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEEEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEVEEEEEEEEEEEEEEEFM         ",
                        "      NGHHHHHHHHHHWHHHHHHHHHHHHHHHIM         ",
                        "      TKKKKKKKKKKKYKKKKKKKKKKKKKKKKU         ",
                        "                                             ", ]

        self.level_5 = ["                                             ",
                        "      RPPPPPPPPPPPZPPPPPPPPPPPPPPPPS         ",
                        "      NABBBBBBBBBBWBBBBBBBBBBBBBBBCM         ",
                        "      NDEEEEEEEEEEWEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEXEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEEEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEVEEEEEEEEEEEEEEEFM         ",
                        "      NGHHHHHHHHHHWHHHHHHHHHHHHHHHIM         ",
                        "      TKKKKKKKKKKKYKKKKKKKKKKKKKKKKU         ",
                        "                                             ", ]

        self.levels = [self.level_0, self.level_1, self.level_2,
                       self.level_3, self.level_4, self.level_5]


class Level_decor:
    def __init__(self) -> None:
        self.level_0_decore = ["                                             ",
                               "                                             ",
                               "                                             ",
                               "                                             ",
                               "           WI       WI       WI              ",
                               "           ND       ND       ND              ",
                               "                 T T                         ",
                               "                                             ",
                               "                                             ",
                               "                                             ", ]

        self.level_1_decore = ["                                             ",
                               "                                             ",
                               "                                             ",
                               "                                             ",
                               "           WI       WI       WI              ",
                               "           ND       ND       ND              ",
                               "                                             ",
                               "                                             ",
                               "                                             ",
                               "                                             ", ]

        self.level_2_decore = ["                                             ",
                               "                                             ",
                               "                                             ",
                               "                                             ",
                               "           WI       WI       WI              ",
                               "           ND       ND       ND              ",
                               "                                             ",
                               "                                             ",
                               "                                             ",
                               "                                             ", ]

        self.level_3_decore = ["                                             ",
                               "                                             ",
                               "                                             ",
                               "                                             ",
                               "           WI       WI       WI              ",
                               "           ND       ND       ND              ",
                               "                 T                           ",
                               "                                             ",
                               "                                             ",
                               "                                             ", ]

        self.level_4_decore = ["                                             ",
                               "                                             ",
                               "                                             ",
                               "                                             ",
                               "           WI       WI       WI              ",
                               "           ND       ND       ND              ",
                               "                 T                           ",
                               "                                             ",
                               "                                             ",
                               "                                             ", ]

        self.level_5_decore = ["                                             ",
                               "                                             ",
                               "                                             ",
                               "                                             ",
                               "           WI       WI       WI              ",
                               "           ND       ND       ND              ",
                               "                 T                           ",
                               "                                             ",
                               "                                             ",
                               "                                             ", ]

        self.levels = [self.level_0_decore, self.level_1_decore, self.level_2_decore,
                       self.level_3_decore, self.level_4_decore, self.level_5_decore]
