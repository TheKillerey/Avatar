#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Glaciers_Galaxies_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Glaciers_Galaxies_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Glaciers_Galaxies_A.TFT_ArenaSkin_Galaxy1.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Middle_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Middle_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Rock_middle_A.TFT_ArenaSkin_DarkStar.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Floaty_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Floaty_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Rock_Floaty_A.TFT_ArenaSkin_DarkStar.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Translate_Range"
                value: vec4 = { 0, 50, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bobbing_Rate"
                value: vec4 = { 0.300000012, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Secondary_Rotation_Rate"
                value: vec4 = { 0.138999999, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "RotationalAxis_Primary"
                value: vec4 = { 0.5, 0, 1, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "RotationAngle_Primary"
                value: vec4 = { -0.0199999996, 0.0199999996, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "RotationAngle_Secondary"
                value: vec4 = { -0.0799999982, 0.0799999982, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "RotationalAxis_Secondary"
                value: vec4 = { 0.699999988, 1, -0.300000012, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Translate_Axis"
                value: vec4 = { 0, 1, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_RANDOM_SECONDARY_MOTION"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/ENV_FloatingObjects"
                    }
                }
            }
        }
        0xe251b20a: bool = false
    }
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Bench_Slab_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Bench_Slab_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Bench_Slab_A.TFT_ArenaSkin_DarkStar.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Flat_Top_C_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Flat_Top_C_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Rock_Flat_Top_C.TFT_ArenaSkin_DarkStar.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Facade_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Facade_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Rock_Facade_A.TFT_ArenaSkin_DarkStar.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Blackhole_Rock_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Blackhole_Rock_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Blackhole_Rock_A.TFT_ArenaSkin_DarkStar.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Tall_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Tall_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Rock_Tall_A.TFT_ArenaSkin_DarkStar.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Galaxy/Materials/Default/Board_Dreadnova_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Galaxy/Materials/Default/Board_Dreadnova_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Galaxy/Textures/Board_Dreadnova_A.TFT_ArenaSkin_Galaxy2.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Galaxy/Materials/Default/Goldmine_Base_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Galaxy/Materials/Default/Goldmine_Base_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Galaxy/Textures/Goldmine_Base_A.TFT_ArenaSkin_Galaxy1.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Trim_Sheet_Metal_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Trim_Sheet_Metal_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Trim_Sheet_Metal_A.TFT_ArenaSkin_Galaxy2.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Jet_Clean_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Jet_Clean_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Jet_Clean_A.TFT_ArenaSkin_Odyssey.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Jet_Dreadnova_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Jet_Dreadnova_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Jet_Dreadnova_A.TFT_ArenaSkin_Galaxy2.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/VFX_Dreadnova" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xe1b2dd4a = MapParticle {
                system: link = "Maps/Particles/TFT/Shared/TFT_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1919.56641, 0.000244140625, 1987.96899, 1
                }
                name: string = "TFT_Wind2"
            }
            0x45214337 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/Dreadnova/TFT_Galaxy_Dreadnova_Screen"
                transform: mtx44 = {
                    0.423649907, 0.102299005, 0.412378013, 0
                    0.547839642, 0.0661390051, -0.579221308, 0
                    -0.1802665, 0.981883645, -0.05838269, 0
                    873.724243, 86.7752991, 1469.1178, 1
                }
                name: string = "TFT_Galaxy_Dreadnova_Screen1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/VFX_Dreadnova"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Shared_v2" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x2ff7cdaf = null
            0x280cca76 = null
            0x8428f883 = null
            0xe30670d4 = null
            0x2b87a377 = null
            0xbb931b41 = null
            0x4cbd628a = null
            0x42024cef = null
            0x53ed22c7 = null
            0x094349ef = null
            0xb1d8cef4 = null
            0xf4b61a8f = null
            0xab595e64 = null
            0x05717daa = null
            0x329adcec = null
            0x79acf00c = null
            0xf043b4b5 = null
            0xd6d5733c = null
            0xa8d44455 = null
            0x019b834d = null
            0x1d77da53 = null
            0xb7e917a0 = null
            0x9297418f = null
            0x3b47d4bd = null
            0x17bc3116 = null
            0xee65b0c2 = null
            0x35a36457 = null
            0xeff8da4b = null
            0x7a3df143 = null
            0x5d77c8c4 = null
            0x1a238f12 = null
            0xfe47d27d = null
            0x56565a88 = null
            0x5ca62bc1 = null
            0xc1006eb1 = null
            0x9bd2715d = null
            0x30c93fa1 = null
            0x7d0e7eab = null
            0x3cd8e0f7 = null
            0x42e3d592 = null
            0xbb52d822 = null
            0x3467a2ff = null
            0xb4c99a87 = null
            0x20ca2a2c = null
            0x5b9cd197 = null
            0x434c84c3 = null
            0x52bbeec2 = null
            0x41c52df6 = null
            0x7399c8da = null
            0xefebf928 = null
            0x7551669f = null
            0x6158c9cf = null
            0x2a7774db = null
            0xa4682294 = null
            0x35e6a257 = MapGroup {
                members: list2[string] = {
                    "c451d051-0d2c-4840-91db-65cfd0df1ec1"
                    "26320d51-b0c6-4d9e-adcd-c3d70889d47d"
                }
                name: string = "group15"
            }
            0x44ff912f = null
            0x3e7970d3 = null
            0x25191500 = null
            0xd4fe640a = MapGroup {
                members: list2[string] = {
                    "73947327-75ac-4800-a52d-47e55caf6a79"
                    "9b30e97a-0edf-4cc1-8a73-3cf21c10dd03"
                    "8baed65f-fb57-4b67-ac97-06a00c57a686"
                    "ce2b35da-f683-4a24-8e5c-c34d4dcb6230"
                }
                name: string = "group19"
            }
            0x5ceac25e = null
            0xca57d935 = null
            0xd675623d = null
            0x7472518f = null
            0xc09e1860 = null
            0x3b78fc17 = null
            0x55126cee = null
            0xbbbf5dc0 = null
            0x757650c5 = null
            0xbf1f198e = null
            0xfaef2fbb = null
            0xe855532b = null
            0x920c4873 = null
            0xfcceb49c = null
            0xd7472490 = null
            0x38c82321 = null
            0x59e7c7ef = null
            0xa632e126 = null
            0x4a3bc502 = null
            0xebb4e9b7 = null
            0x649d4d0c = null
            0xba60e39c = null
            0xa8f7297b = null
            0xb9c1383c = null
            0x8f60e8ce = null
            0xbb0e8c04 = null
            0x50442457 = null
            0x537b4715 = null
            0x59c7108b = null
            0x60bc0146 = null
            0xe525996b = null
            0x13d941ee = null
            0x453319f6 = null
            0x6c4a33d5 = null
            0x302c2c48 = null
            0x142d9399 = null
            0x67613649 = null
            0x29d03e8c = null
            0x11763954 = null
            0xe6806b2a = null
            0x4eec50de = null
            0xec7ee90d = null
            0x245334ad = null
            0x5d148095 = null
            0xb8b46272 = null
            0xb19fcaf8 = null
            0xebe9512f = null
            0x953ab1a9 = null
            0xc71b37f3 = null
            0x1d409379 = MapGroup {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 0.948094666, 0
                    2995.67822, -339.70752, 2667.89282, 1
                }
                name: string = "group1"
            }
            0x9093d129 = null
            0x45fb23c1 = null
            0xe873784e = null
            0x91603791 = null
            0x3fdf3804 = null
            0xb3299236 = null
            0x235b2294 = null
            0xcc475dcc = null
            0x53aae39c = null
            0xe4b79064 = null
            0xe89a5db0 = null
            0x235bf9ba = null
            0xc7537449 = null
            0xd248423b = null
            0x7353ff5b = null
            0x118a5998 = null
            0x6ef00b3d = null
            0x4fda4f08 = null
            0x2a763665 = null
            0x43bd56ab = null
            0x92469741 = null
            0xc4925fe5 = null
            0x12302de6 = null
            0x3b720783 = null
            0xd8d13bb3 = MapGroup {
                members: list2[string] = {
                    "23ab19f5-6c49-46c8-83c5-474913178f5c"
                    "eb1f8eed-3f53-4fd7-81f1-a30cddf7626f"
                    "a35e5b65-ce0e-459d-a63e-dab864818dcb"
                    "e10cb0a9-4f41-4577-96f1-28d6648e42f2"
                    "7443d31c-69a4-40eb-b899-cfe065714df9"
                    "5e1ba055-eb3d-4a37-b29c-13cceff43f26"
                    "36ba2e5f-890e-4fb2-95ce-12883f3b0275"
                    "64944ff3-77cf-43a0-a53b-433d306ce246"
                    "e000be44-9aa7-4e63-a027-9fdcfece4a64"
                    "a5c3ec42-64cf-458b-a973-d692cb93f30c"
                }
                transform: mtx44 = {
                    -3.57627869e-07, 0, 1, 0
                    0, 1, 0, 0
                    -1, 0, -3.57627869e-07, 0
                    1699.83521, -118.505661, 409.408142, 1
                }
                name: string = "group5"
            }
            0xa6f078fa = null
            0xadd350c9 = null
            0x56b79bfe = null
            0xbc4d3603 = null
            0x9c6278b9 = null
            0xcf2d26a9 = null
            0x1c3b32ad = null
            0x4594fd09 = null
            0xbd178575 = null
            0x70bd1a2e = null
            0xd17f1116 = null
            0x7ca7fe0f = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Shared_v2"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Dreadnova" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xe111df69 = null
            0x4e00f99a = null
            0x1d9c9492 = null
            0x9043dc57 = null
            0x37321448 = null
            0x276067c9 = null
            0x0bb6b32a = null
            0xe40b00d6 = null
            0xea8083c1 = null
            0xf09f2bf8 = null
            0x9feb5a65 = null
            0x0820023d = null
            0x60a8dc9c = null
            0xd74bf065 = null
            0x4431e56a = null
            0x490813fe = null
            0x1c420400 = null
            0xdb0ec2f6 = null
            0x4216ba90 = null
            0x34d054c1 = null
            0x2fef6b6b = null
            0x2abe929d = null
            0xf7f2857a = null
            0x55858498 = null
            0x43563fbd = null
            0xebdecca6 = null
            0x947e84b2 = null
            0x0e763cb2 = null
            0xeb2c9cc4 = null
            0xb7b3ddbf = null
            0x9b05d4ec = null
            0x3cd884c5 = null
            0x37b29596 = null
            0x38c2f539 = null
            0xed0594c7 = null
            0x51da5968 = null
            0x0a18771c = null
            0x4a5666e9 = null
            0xb37406d4 = null
            0x4e916fbe = null
            0xf3a78175 = null
            0x6cc9e5d6 = null
            0x361ac41c = null
            0x843544b8 = null
            0xa360aec5 = null
            0x137f6937 = null
            0x9e1bcaec = null
            0x553265a9 = null
            0x6bddc7c0 = null
            0x4f8d3122 = null
            0x86e1d6c7 = null
            0x58e551ba = null
            0x89917f26 = null
            0xdef3a26e = null
            0xabf7ad8b = MapGroup {
                members: list2[string] = {
                    "9339797d-3d87-4ffd-89fb-d93b3fa4fab7"
                }
                name: string = "group8"
            }
            0x4dc2f971 = null
            0x5acb851c = null
            0x2252d708 = null
            0xdb09c7fe = null
            0x625c8c08 = null
            0x121739e5 = null
            0xaa11f440 = null
            0x327f23a1 = null
            0x47d462ef = null
            0xb0d0650a = null
            0x6ce1227e = null
            0x8e75ae0b = null
            0xfe0f93ed = null
            0xc32d73af = null
            0x6e1ac813 = null
            0x2871a9c1 = null
            0x7e69fb35 = null
            0xe67cbac4 = null
            0x2fd78c6b = null
            0xeadff9ec = null
            0x2e865179 = null
            0x578822ae = null
            0x17743ec1 = null
            0xfa9c29d5 = null
            0x25710406 = null
            0x091b31de = null
            0x102ca933 = MapGroup {
                name: string = "group9"
            }
            0xc0e50073 = null
            0xb956a1be = null
            0x68db4613 = null
            0xe854340a = null
            0xc20014fe = null
            0x555c1a73 = null
            0xa1adcf0a = null
            0x80563062 = null
            0xb7cc7a8e = null
            0x00d68cb3 = null
            0x58230bc9 = null
            0x97895d1f = null
            0x088df2ae = null
            0x8d16e841 = null
            0x1a09a3a1 = MapGroup {
                members: list2[string] = {
                    "af4097ae-54f4-43ba-b625-3f78b72e1a50"
                }
                name: string = "group10"
            }
            0x881d97a8 = null
            0x7cc12947 = null
            0x14d92b05 = null
            0x2558883b = null
            0x25d621c9 = null
            0x3d8a8c6b = null
            0x79976db4 = null
            0xb1f7267a = MapGroup {
                members: list2[string] = {
                    "c927ecb3-0122-4324-b613-bfae55df7fae"
                }
                name: string = "group11"
            }
            0x06e5740a = null
            0xc71dee8c = null
            0xdd8be310 = null
            0xff1823d9 = null
            0x230fb1cf = null
            0xa95130ad = null
            0x358f3339 = null
            0xb7ca7c0b = null
            0x9e15cc84 = null
            0x10ebff5e = null
            0x50f6b355 = null
            0xa6489472 = null
            0xa79d27db = null
            0x44737cd2 = null
            0x41d79b27 = null
            0x4e345904 = null
            0x80cffb03 = null
            0x3541d190 = null
            0xe50edd0a = null
            0xcfe6b295 = null
            0x60bc092d = null
            0x3259583a = null
            0x0be82dca = null
            0x96cfb7a1 = MapGroup {
                members: list2[string] = {
                    "1b5c87bf-aa92-4e18-a14f-58768133926f"
                    "263b51fd-6ad6-4710-8cd4-472bfef57cd6"
                }
                name: string = "group12"
            }
            0x31d6be88 = null
            0x0522877f = null
            0x0be16696 = null
            0xa8f5e931 = null
            0xa5cb9a5e = null
            0x69b47568 = null
            0x8a658683 = null
            0x3943dbb6 = null
            0xaa698989 = null
            0xf59cce5b = null
            0x1565bad5 = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Dreadnova"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Dreadnova_Skybox" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xdb39793b = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/Dreadnova/TFT_Skybox_Dreadnova_A"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1987.25806, 0.0009765625, 2051.75488, 1
                }
                name: string = "TFT_Skybox_CrashSite_A2"
                0xccf79327: u8 = 126
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Dreadnova_Skybox"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Galaxy_Design_Base_v2" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xf7e857de = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Spawn_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2942.92432, 11.2485962, 2437.69849, 1
                }
                name: string = "GoldMineLocatorAway"
            }
            0x9b9787df = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1067.23218, 11.2485962, 1695.15454, 1
                }
                name: string = "GoldMineLocator"
            }
            0x4bff90c5 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2801, 0, 2911.16626, 1
                }
                name: string = "BenchAwayLocator"
            }
            0x90883f04 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1187.73376, 0, 1111.19238, 1
                }
                name: string = "BenchHomeLocator"
            }
            0x4cb64046 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3021.10547, 0, 2859.89062, 1
                }
                name: string = "ItemBenchAwayLocator"
            }
            0x1cd3dd02 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    856.235291, 0, 1091.79797, 1
                }
                name: string = "ItemBenchLocator"
            }
            0x2f580834 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1421.01526, 0, 1458, 1
                }
                name: string = "BoardLocator"
            }
            0x717bb0ac = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1956.11304, 0, 1628.69995, 1
                }
                name: string = "Camera_Island"
            }
            0xf874b8e7 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -1, -8.74227766e-08, 0, 0
                    -8.74227766e-08, 1, -8.74227766e-08, 0
                    7.64274186e-15, -8.74227766e-08, -1, 0
                    2067, 0, 2427.01318, 1
                }
                name: string = "Camera_Flipped_Island"
            }
            0xe9d84b9b = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1102.27698, 0, 1388.43628, 1
                }
                name: string = "PerchLocator"
            }
            0x58f4606b = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2857.91894, 0, 2664.4563, 1
                }
                name: string = "PerchAwayLocator"
            }
            0xe1404aa4 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2000, 0, 2000, 1
                }
                name: string = "BoardCenterLocator"
            }
            0xc723a0b3 = MapCamera {
                0x563a1941: f32 = 3700
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2056.11304, 0, 1700.69995, 1
                }
                name: string = "Camera_TFT_IslandHome_PC"
            }
            0xd0ce0321 = MapCamera {
                0x563a1941: f32 = 3700
                yaw: f32 = 180
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1967, 0, 2355, 1
                }
                name: string = "Camera_TFT_IslandAway_PC"
            }
            0x7fd48cc3 = MapCamera {
                0x6f3e4327: f32 = 1200
                0x563a1941: f32 = 3180
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1956.11304, 0, 1920.69995, 1
                }
                name: string = "Camera_TFT_IslandHome_Mobile"
            }
            0xb9b64b31 = MapCamera {
                0x6f3e4327: f32 = 1200
                0x563a1941: f32 = 3180
                yaw: f32 = 180
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2067, 0, 2135, 1
                }
                name: string = "Camera_TFT_IslandAway_Mobile"
            }
            0x608bfae5 = MapCamera {
                0x563a1941: f32 = 4500
                pitch: f32 = 41
                FieldOfView: f32 = 55
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2056.11304, 0, 1700.69995, 1
                }
                name: string = "Camera_TFT_StoreView"
            }
            0x2e12e907 = MapCamera {
                0x563a1941: f32 = 4500
                pitch: f32 = 89.9000015
                FieldOfView: f32 = 55
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2056.11304, 100, 1700.69995, 1
                }
                name: string = "Camera_TFT_StoreThumb"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Galaxy_Design_Base_v2"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/LightingVolume_Dreadnova" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x87599553 = MapLightingVolume {
                sunColor: vec4 = { 0.282352954, 0.301960796, 0.333333343, 0.972549021 }
                sunDirection: vec3 = { 0.150000006, 0.827000022, 0.150000006 }
                0xd8851203: f32 = 15
                0xba02f116: f32 = 0.100000001
                skyLightColor: vec4 = { 0.368627459, 0.313725501, 0.372549027, 1 }
                horizonColor: vec4 = { 0.470588237, 0.411764711, 0.396078438, 1 }
                groundColor: vec4 = { 0.411764711, 0.278431386, 0.266666681, 1 }
                skyLightScale: f32 = 0.75
                lightMapColorScale: f32 = 2
                fogColor: vec4 = { 0.239215687, 0.156862751, 0.172549024, 1 }
                fogAlternateColor: vec4 = { 0.290196091, 0.0784313753, 0.0784313753, 1 }
                fogStartAndEnd: vec2 = { 250, -600 }
                transform: mtx44 = {
                    2835.39404, 0, 0, 0
                    0, 4314.72998, 0, 0
                    0, 0, 3081.94995, 0
                    2186.59424, -927.355957, 2144.35596, 1
                }
                name: string = "LightingVolume1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/LightingVolume_Dreadnova"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Audio_CrashSite_Dreadnova" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x64eb94c9 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/Common/TFT_Audio-Emitter_Galaxy_Outdoor_Amb_Loop"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1868.32385, 151.125488, 2276.11743, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_Outdoor_Amb_Loop1"
            }
            0x75b783cb = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_RadioFutz"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1240.54639, -6.10351562e-05, 1689.77808, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_CrashSite_Jet_RadioFutz1"
            }
            0x2ffc388e = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Sparking"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1134.70581, 130.737122, 1834.13306, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Sparking1"
            }
            0x0e38859e = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Alarm"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1150.68738, 80.9458008, 1486.78577, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Alarm1"
            }
            0x5470e172 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Engine"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    995.01355, 4.29052734, 1646.20325, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Engine1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Audio_CrashSite_Dreadnova"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Lighting_Dreadnova" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x4379cb9a = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 3.27487636
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -215.669373, 1489.16211, 2391.27197, 1
                }
                name: string = "Freljord_FG_Fill6"
            }
            0xf4e6081b = MapPointLight {
                type: link = 0x4ddca076
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2555.59009, 804.190735, 118.002289, 1
                }
                name: string = "Light_Point_Center_DragonCloud1"
            }
            0x6e957fc8 = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 1.6396029
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    982.884888, 267.677185, 3573.90698, 1
                }
                name: string = "Freljord_FG_Fill7"
            }
            0x73a1313f = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 1.70631826
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2956.29688, 648.424683, 1413.16748, 1
                }
                name: string = "Freljord_FG_Fill8"
            }
            0xcfb1d4c3 = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 1.6396029
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    814.627197, 115.615082, 1132.96826, 1
                }
                name: string = "Freljord_FG_Fill9"
            }
            0x27a348ea = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 1.89963698
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2670.98144, 289.476013, 3688.99634, 1
                }
                name: string = "Freljord_FG_Fill10"
            }
            0x640e246e = MapPointLight {
                type: link = 0xf70c338d
                radiusScale: f32 = 1.72811496
                intensityScale: f32 = 1.29999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1641.5083, -166.967377, 488.554016, 1
                }
                name: string = "ReddishBrown_Point_A"
            }
            0x70858474 = MapPointLight {
                type: link = 0x3b3506ed
                radiusScale: f32 = 1.67512548
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1947.43298, 384.388824, 1081.46399, 1
                }
                name: string = "SoftWhite_Point_Reality1"
            }
            0xdebe0764 = MapPointLight {
                type: link = 0x3b3506ed
                radiusScale: f32 = 1.67512548
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2019.51501, 450.754883, 3014.87964, 1
                }
                name: string = "SoftWhite_Point_Reality2"
            }
            0xc95e869c = MapPointLight {
                type: link = 0x3b3506ed
                radiusScale: f32 = 1.64999998
                intensityScale: f32 = 1.20000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1140.05103, 333.885681, 1433.90405, 1
                }
                name: string = "SoftWhite_Point_Reality3"
            }
            0xf006a425 = MapPointLight {
                type: link = 0x3b3506ed
                radiusScale: f32 = 1.24185896
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2865.42993, 353.50589, 2652.13599, 1
                }
                name: string = "SoftWhite_Point_Reality4"
            }
            0x15f3a2ba = MapPointLight {
                type: link = 0xf70c338d
                radiusScale: f32 = 1.72811496
                intensityScale: f32 = 1.29999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    123.962891, -235.269943, 1290.32898, 1
                }
                name: string = "ReddishBrown_Point_A1"
            }
            0xb5d28c52 = MapPointLight {
                type: link = 0xf70c338d
                radiusScale: f32 = 1.72811496
                intensityScale: f32 = 1.29999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -242.631775, -235.269943, 2468.55542, 1
                }
                name: string = "ReddishBrown_Point_A2"
            }
            0x5c676870 = MapPointLight {
                type: link = 0xf70c338d
                radiusScale: f32 = 1.72811496
                intensityScale: f32 = 1.29999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4.74786377, -235.269943, 3011.41357, 1
                }
                name: string = "ReddishBrown_Point_A3"
            }
            0x718405cd = MapPointLight {
                type: link = 0xf70c338d
                radiusScale: f32 = 1.72811496
                intensityScale: f32 = 1.29999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1555.72058, -235.269943, 3856.62988, 1
                }
                name: string = "ReddishBrown_Point_A4"
            }
            0xfc896daa = MapPointLight {
                type: link = 0xf70c338d
                radiusScale: f32 = 1.72811496
                intensityScale: f32 = 1.29999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3889.74048, -235.269943, 2304.08545, 1
                }
                name: string = "ReddishBrown_Point_A5"
            }
            0x7b697ee0 = MapPointLight {
                type: link = 0xf70c338d
                radiusScale: f32 = 1.72811496
                intensityScale: f32 = 1.29999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3990.32251, -235.269943, 1424.63208, 1
                }
                name: string = "ReddishBrown_Point_A6"
            }
            0x9acf572a = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 2.75
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2000, 478, 2033, 1
                }
                name: string = "Freljord_FG_Fill1"
            }
            0x97cf8629 = MapPointLight {
                type: link = 0x4ddca076
                radiusScale: f32 = 0.749999702
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1889.85474, 17.9444733, 704.03418, 1
                }
                name: string = "Light_Point_Center_DragonCloud2"
            }
            0x0c398dea = MapPointLight {
                type: link = 0x4ddca076
                radiusScale: f32 = 0.649999976
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1327.48743, 16.4941406, 678.605164, 1
                }
                name: string = "Light_Point_Center_DragonCloud3"
            }
            0x5cda9999 = MapPointLight {
                type: link = 0x4ddca076
                radiusScale: f32 = 0.649999976
                intensityScale: f32 = 0.649999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2405.42163, 4.14363098, 654.433533, 1
                }
                name: string = "Light_Point_Center_DragonCloud4"
            }
            0x1952e31f = MapPointLight {
                type: link = 0x4ddca076
                radiusScale: f32 = 0.649999976
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    662.801819, 376.181335, 1649.85974, 1
                }
                name: string = "Light_Point_Center_DragonCloud5"
            }
            0x9ef74a53 = MapPointLight {
                type: link = 0xf70c338d
                radiusScale: f32 = 2.5
                intensityScale: f32 = 1.29999995
                transform: mtx44 = {
                    1.25, 0, 0, 0
                    0, 1.25, 0, 0
                    0, 0, 1.25, 0
                    1985.73596, 349.190002, 2042.96997, 1
                }
                name: string = "ReddishBrown_Point_A7"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Lighting_Dreadnova"
    }
    "Maps/MapGeometry/Map22/Galaxy_Dreadnova" = mapContainer {
        mapPath: string = "Maps/MapGeometry/Map22/Galaxy_Dreadnova"
        components: list[pointer] = {
            MapSunProperties {
                sunColor: vec4 = { 0.525490224, 0.349019617, 0.368627459, 1 }
                sunDirection: vec3 = { -0.385433108, 0.828491211, -0.406255662 }
                0xd8851203: f32 = 75
                skyLightColor: vec4 = { 0.596078455, 0.392156869, 0.376470596, 1 }
                horizonColor: vec4 = { 0.447058827, 0.301960796, 0.290196091, 1 }
                groundColor: vec4 = { 0.352941185, 0.235294119, 0.262745112, 1 }
                skyLightScale: f32 = 1
                fogEnabled: bool = false
                fogColor: vec4 = { 0.100007631, 0.059998475, 0.110002287, 1 }
                fogAlternateColor: vec4 = { 0.420004576, 0.379995435, 0.420004576, 1 }
                fogStartAndEnd: vec2 = { -1000, -20000 }
                fogEmissiveRemap: f32 = 1
                useBloom: bool = true
            }
            MapBakeProperties {
                0x22d24a9a: f32 = 0.850000024
                lightGridCharacterFullBrightIntensity: f32 = 0.5
                0x2f3b5471: f32 = 2
                lightGridFileName: string = "ASSETS/Maps/Lightmaps/Maps/MapGeometry/Map22/Galaxy_Dreadnova/LightGrid.TFT_1023_LightingUpdate.dat"
            }
            MapLightingV2 {
                0xee91017d: f32 = 0.899999976
            }
            MapNavGrid {
                0xf7197db9: string = "ASSETS/Maps/NavGrid/Map22/Galaxy_CrashSite_Navgrid.aimesh_ngrid"
            }
        }
        boundsMax: vec2 = { 4000, 4000 }
        0xf010defb: f32 = 5000
        chunks: map[hash,link] = {
            0xb7f539f3 = "Maps/MapGeometry/Map22/Chunks/Galaxy/VFX_Dreadnova"
            0x1a917671 = "Maps/MapGeometry/Map22/Chunks/Galaxy/LightingVolume_Dreadnova"
            0x850e3869 = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Dreadnova_Skybox"
            0xd9d0b55b = "Maps/MapGeometry/Map22/Chunks/Galaxy/Lighting_Dreadnova"
            0x4ab54b56 = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Dreadnova"
            "Art_Shared_v2" = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Shared_v2"
            "Galaxy_Design_Base_v2" = "Maps/MapGeometry/Map22/Chunks/Galaxy/Galaxy_Design_Base_v2"
            "Audio_CrashSite_Dreadnova" = "Maps/MapGeometry/Map22/Chunks/Galaxy/Audio_CrashSite_Dreadnova"
        }
    }
    "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Engine" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/Black.DDS"
                meshRenderFlags: u8 = 0
                texture: string = "ASSETS/Shared/Particles/Black.DDS"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 0
                }
            }
        }
        visibilityRadius: f32 = 1000
        particleName: string = "TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Engine"
        particlePath: string = "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Engine"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_crashsite_jet_engine"
    }
    "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Alarm" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/Black.DDS"
                meshRenderFlags: u8 = 0
                texture: string = "ASSETS/Shared/Particles/Black.DDS"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 0
                }
            }
        }
        visibilityRadius: f32 = 1000
        particleName: string = "TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Alarm"
        particlePath: string = "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Alarm"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_crashsite_jet_alarm"
    }
    "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Sparking" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/Black.DDS"
                meshRenderFlags: u8 = 0
                texture: string = "ASSETS/Shared/Particles/Black.DDS"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 0
                }
            }
        }
        visibilityRadius: f32 = 1000
        particleName: string = "TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Sparking"
        particlePath: string = "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Sparking"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_crashsite_jet_sparking"
    }
    "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_RadioFutz" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/Black.DDS"
                meshRenderFlags: u8 = 0
                texture: string = "ASSETS/Shared/Particles/Black.DDS"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 0
                }
            }
        }
        visibilityRadius: f32 = 1000
        particleName: string = "TFT_Audio-Emitter_Galaxy_CrashSite_Jet_RadioFutz"
        particlePath: string = "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_RadioFutz"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_crashsite_radio_futz"
    }
    "Maps/Particles/TFT/Galaxy/Common/TFT_Audio-Emitter_Galaxy_Outdoor_Amb_Loop" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/Black.DDS"
                meshRenderFlags: u8 = 0
                texture: string = "ASSETS/Shared/Particles/Black.DDS"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 0
                }
            }
        }
        visibilityRadius: f32 = 2000
        particleName: string = "TFT_Audio-Emitter_Galaxy_Outdoor_Amb_Loop"
        particlePath: string = "Maps/Particles/TFT/Galaxy/Common/TFT_Audio-Emitter_Galaxy_Outdoor_Amb_Loop"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_common_amb_loop"
    }
    "Maps/Particles/TFT/Galaxy/Dreadnova/TFT_Skybox_Dreadnova_A" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Base"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -150, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/TFT_Skybox_BackgroundClouds.TFT_ArenaSkin_DarkStar.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.97647059, 0.53725493, 0.874509811, 1 }
                }
                pass: i16 = -10
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 4
                isGroundLayer: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.349999994, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_Stars01.dds"
                texDiv: vec2 = { 2, 2 }
                scaleOverride: vec3 = { 18, 18, 18 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "BlueClouds"
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 150, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/TFT_Skybox_MidgroundClouds.TFT_ArenaSkin_DarkStar.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.859998465, 0.300007641, 0.579995394 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.310002297, 0.680003047, 0.439993888 }
                }
                pass: i16 = -8
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -90, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.0799999982, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.270000011, 0.270000011, 0.270000011 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_BlueCloud.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0199999996, 0 }
                }
                texDiv: vec2 = { 1, 2 }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.800000012, 2 }
                }
                scaleOverride: vec3 = { 17, 17, 17 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Pink01"
                disabled: bool = true
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 180, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/TFT_Skybox_ForegroundClouds.TFT_Set3_Carousel.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.859998465, 0.540001512, 1, 0.340001523 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.829999208, 0.889997721, 1 }
                }
                pass: i16 = -7
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 6, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_PinkCloud.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.100000001, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 2 }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_PinkCloud_Mask.dds"
                scaleOverride: vec3 = { 17, 17, 17 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Pink02"
                disabled: bool = true
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 180, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/TFT_Skybox_ForegroundClouds.TFT_Set3_Carousel.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.200000003, 0.990005314, 1, 0.379995435 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.349996179, 0.910002291, 1, 0.420004576 }
                }
                pass: i16 = -6
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -10, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_PinkCloud.dds"
                textureMult: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_PinkCloud_Mask.dds"
                uvScaleMult: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
                }
                scaleOverride: vec3 = { 17, 17, 17 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Glow"
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 150, -10 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/TFT_Skybox_BackgroundClouds_B.TFT_Set3_Carousel.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.972549021, 0.972549021, 0.972549021, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.549019635, 0.286274523, 1 }
                }
                pass: i16 = -9
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.349999994, 0.300000012, 0.300000012 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/DarkStar_Skybox_Clouds_Glow.dds"
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 2 }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/DarkStar/DarkStar_Skybox_BlueCloud_Mask.dds"
                scaleOverride: vec3 = { 17, 17, 17 }
            }
        }
        visibilityRadius: f32 = 12000
        particleName: string = "TFT_Skybox_Dreadnova_A"
        particlePath: string = "Maps/Particles/TFT/Galaxy/Dreadnova/TFT_Skybox_Dreadnova_A"
        flags: u8 = 197
        hudAnchorPositionFromWorldProjection: bool = false
    }
    "Maps/Particles/TFT/Galaxy/Dreadnova/TFT_Galaxy_Dreadnova_Screen" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                emitterName: string = "screenMeshAdd"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_Screen_Mesh.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.521568656, 0.521568656, 1 }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.600000024, 0.5, 0.5 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_Pixels.TFT_ArenaSkin_Odyssey.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.300000012 }
                }
                texDiv: vec2 = { 2, 2 }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_Static.TFT_ArenaSkin_Odyssey.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.0199999996 }
                }
                birthUVOffsetMult: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.0529999994
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.0529999994
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            4
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11
                }
                emitterName: string = "screenMeshAddFlicker"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_Screen_Mesh.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.721568644, 0.43921569, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0919540226
                            0.0919540226
                            0.101532564
                            0.101532564
                            0.124521069
                            0.124521069
                            0.258620679
                            0.262452096
                            0.312260538
                            0.312260538
                            0.375478923
                            0.375478923
                            0.496168584
                            0.515325665
                            0.557471275
                            0.557471275
                            0.680076599
                            0.680076599
                            0.703065157
                            0.703065157
                            0.727969348
                            0.735632181
                            0.78927201
                            0.78927201
                            0.827586234
                            0.827586234
                            0.936781585
                            0.938697338
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.721568644, 0.43921569, 0 }
                            { 1, 0.721568644, 0.43921569, 0 }
                            { 1, 0.721568644, 0.43921569, 1 }
                            { 1, 0.721568644, 0.43921569, 1 }
                            { 1, 0.721568644, 0.43921569, 0 }
                            { 1, 0.721568644, 0.43921569, 0 }
                            { 1, 0.721568644, 0.43921569, 1 }
                            { 1, 0.721568644, 0.43921569, 1 }
                            { 1, 0.721568644, 0.43921569, 0 }
                            { 1, 0.721568584, 0.43921569, 0 }
                            { 1, 0.721568584, 0.43921569, 1 }
                            { 1, 0.721568584, 0.43921569, 1 }
                            { 1, 0.721568584, 0.43921569, 0 }
                            { 0.99999994, 0.721568584, 0.43921566, 0.990291238 }
                            { 0.99999994, 0.721568584, 0.43921566, 0.990291238 }
                            { 0.99999994, 0.721568584, 0.43921566, 0 }
                            { 0.99999994, 0.721568584, 0.43921566, 1 }
                            { 0.99999994, 0.721568584, 0.43921566, 1 }
                            { 0.99999994, 0.721568584, 0.43921566, 0 }
                            { 0.99999994, 0.721568584, 0.43921566, 0 }
                            { 0.99999994, 0.721568584, 0.43921566, 1 }
                            { 0.99999994, 0.721568584, 0.43921566, 0 }
                            { 0.99999994, 0.721568584, 0.43921566, 0.990291238 }
                            { 0.99999994, 0.721568584, 0.43921566, 0 }
                            { 0.99999994, 0.721568584, 0.43921566, 1 }
                            { 1, 0.721568644, 0.43921569, 1 }
                            { 1, 0.721568644, 0.43921569, 0 }
                            { 1, 0.721568644, 0.43921569, 0 }
                            { 1, 0.721568644, 0.43921569, 0.980582535 }
                            { 1, 0.721568644, 0.43921569, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.600000024, 0.5, 0.5 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_Pixels.TFT_ArenaSkin_Odyssey.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.300000012 }
                }
                texDiv: vec2 = { 2, 2 }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 180
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_Static.TFT_ArenaSkin_Odyssey.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.0199999996 }
                }
                birthUVOffsetMult: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.400000006
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            6
                        }
                    }
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "jjFlare"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 10, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.519996941, 0.519996941, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.519996941, 0.519996941, 0 }
                            { 1, 0.519996941, 0.519996941, 1 }
                            { 1, 0.519996941, 0.519996941, 0 }
                        }
                    }
                }
                pass: i16 = 5
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 200, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 300, 200, 50 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Slash_Flare.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "glowLight"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 0, 100 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.200000003, 0, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.200000003, 0, 0 }
                            { 1, 0.200000003, 0, 0.500007629 }
                            { 1, 0.200000003, 0, 0 }
                        }
                    }
                }
                pass: i16 = 500
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 100
                }
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 400, 50 }
                }
                texture: string = "ASSETS/Shared/Particles/Base_Light_Hard_Edge.dds"
            }
        }
        particleName: string = "TFT_Galaxy_Dreadnova_Screen"
        particlePath: string = "Maps/Particles/TFT/Galaxy/Dreadnova/TFT_Galaxy_Dreadnova_Screen"
    }
    "Maps/Particles/TFT/Shared/TFT_Wind" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 12
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            12
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "Wind"
                disabled: bool = true
                importance: u8 = 0
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 1 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/Env_MB_highWind_01.sco"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 45, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 1, 3 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    3
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 1, 3 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_highWind_01.SRE_Base.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0.100000001
                                    0.100000001
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: string = "ASSETS/Particles/ChoDino_Dust.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.400000006, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0.400000006
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.400000006
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            4
                        }
                    }
                }
                emitterName: string = "Wind1"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/Env_MB_bridgeWind_SE_02.SRE_Base.sco"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.611764729, 0.333333343, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10.5, 4.5, 7.5 }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_bridgeWind_SE_02.SRE_Base.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.449999988, 0 }
                }
            }
        }
        visibilityRadius: f32 = 1500
        particleName: string = "TFT_Wind"
        particlePath: string = "Maps/Particles/TFT/Shared/TFT_Wind"
    }
    0x3b3506ed = MapPointLightType {
        lightColor: vec4 = { 0.905882359, 0.90196079, 0.854901969, 1 }
        Impact: i32 = 1
    }
    0xf70c338d = MapPointLightType {
        lightColor: vec4 = { 0.654901981, 0, 0, 1 }
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0x4ddca076 = MapPointLightType {
        radius: f32 = 800
        Impact: i32 = 1
    }
    0xae60cac5 = MapPointLightType {
        lightColor: vec4 = { 0.717647076, 0.211764708, 0.329411775, 1 }
        radius: f32 = 497
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
}
