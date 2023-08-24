
tile_size = 64


class Level_data:
    def __init__(self) -> None:
        self.level_0 = ["                                             ",
                        "      RPPPPPPPPPPPZPPPPPPPPPPPPPPPPS         ",
                        "      NABBBBBBBBBBWBBBBBBBBBBBBBBBCM         ",
                        "      NDEEEEEEEEEEXEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEBEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEHHHEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEVEEEEEEEEHEEEEEEFM         ",
                        "      NGHHHHHHHHHHWHHHHHHHHVHHHHHHIM         ",
                        "      TKKKKKKKKKKKYKKKKKKKKYKKKKKKKU         ",
                        "                                             ", ]

        self.level_1 = ["                                             ",
                        "      RPPPPPZPPPPPPPZPPPPPPPPPPPPPPS         ",
                        "      NABBBBXBBBBBBBXBBBBBBBBBBBBBCM         ",
                        "      NDEEEEBEEEEEEEBEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEEEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEHHHHHHHHHEEEEEEEEEEEHHIM         ",
                        "      NDEEEEV       VEEEEEEEEEHHEEFM         ",
                        "      NGHHHHW       WHHHHHHHHHHHHHIM         ",
                        "      TKKKKKU       TKKKKKKKKKKKKKKU         ",
                        "                                             ", ]

        self.level_2 = ["                                             ",
                        "      RPPPPPS               RPPPPPPS         ",
                        "      NABBBCM               NABBBBCM         ",
                        "      NDEEEFM               NDEEEEFM         ",
                        "      NDEEEFM               TDEEEEFM         ",
                        "      NDEEEFU                DEEEEFM         ",
                        "      NDEEEF                VDEEEEFM         ",
                        "      NGHHHI                WGHHHHIM         ",
                        "      TKKKKKU               TKKKKKKU         ",
                        "                                             ", ]

        self.level_3 = ["                                             ",
                        "      RPPPPPPPPPPPPPPPPPPPPPPPPPPPPS         ",
                        "      NABBBBBBBBBBBBBBBBBBBBBBBBBBCM         ",
                        "      NDEEEEEEEEEEEEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEEEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEEEEEEEEEEEEEEEEEFM         ",
                        "      NDEEEEEEEEEEEEEEEEEEEEEEEEEEFM         ",
                        "      NGHHHHHHHHHHHHHHHHHHHHHHHHHHIM         ",
                        "      TKKKK                    KKKKU         ",
                        "                                             ", ]

        self.level_4 = ["                                             ",
                        "      RPPPPPPPPPPZPPPPPPPPPPPZPPPPPS         ",
                        "      NABBBBBBBBCWABBBBBBBBBCWABBBCM         ",
                        "      NDEEEEEEEEFWDEEEEEEEEEFWDEEEFM         ",
                        "      NDEEEEEEEEFXDEEEEEEEEEFXDEEEFM         ",
                        "      NDEEEFVDEEEBEEEEFVDEEEEBEEEEFM         ",
                        "      NDEEEFWDEEEEEEEEFWDEEEEEEEEEFM         ",
                        "      NGHHHIWGHHHHHHHHIWGHHHHHHHHHIM         ",
                        "      TKKKKKYKKKKKKKKKKYKKKKKKKKKKKU         ",
                        "                                             ", ]

        self.levels = [self.level_0, self.level_1, self.level_2,
                       self.level_3, self.level_4]


class Level_decor:
    def __init__(self) -> None:
        self.level_0_decore = ["                                             ",
                               "                                             ",
                               "              F           F                  ",
                               "              G           G                  ",
                               "           WI S     WI    S  WI              ",
                               "           ND       ND       ND              ",
                               "                 T T                         ",
                               "                                             ",
                               "                                             ",
                               "                                             ", ]

        self.level_1_decore = ["                                             ",
                               "                                             ",
                               "           F               F                 ",
                               "           G               G                 ",
                               "        WI S   WI      WI  S WI              ",
                               "        ND     ND      ND    ND              ",
                               "             TTTTTTT            TTT          ",
                               "                              TT             ",
                               "                                             ",
                               "                                             ", ]

        self.level_2_decore = ["                                             ",
                               "                                             ",
                               "          F                   F              ",
                               "          G                   G              ",
                               "        WIS                   SWI            ",
                               "        ND                     ND            ",
                               "                     TT   TT                 ",
                               "                 TT                          ",
                               "             TT                              ",
                               "                                             ", ]

        self.level_3_decore = ["                                             ",
                               "                                             ",
                               "           F     F    F    F                 ",
                               "           G     G    G    G                 ",
                               "        WI S  WI S    S WI S    WI            ",
                               "        ND    ND        ND      ND            ",
                               "                    TT  TTT                  ",
                               "               TTT                           ",
                               "           TT                TT              ",
                               "                                             ", ]

        self.level_4_decore = ["                                             ",
                               "                                             ",
                               "          F           F                      ",
                               "          G           G                      ",
                               "        WIS        WI S  WI                  ",
                               "        ND         ND    ND                  ",
                               "              TT    TT   TT     TTT          ",
                               "                                             ",
                               "                                             ",
                               "                                             ", ]

        self.levels = [self.level_0_decore, self.level_1_decore, self.level_2_decore,
                       self.level_3_decore, self.level_4_decore]
