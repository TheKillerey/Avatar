#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Maps/KitPieces/Howling_Abyss/Materials/lambert4165_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/lambert4165_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/prop_woodbeams.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/SB_Wall_E_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/SB_Wall_E_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/structure_base_wall_E.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/BK_periph_ice_cu2_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/BK_periph_ice_cu2_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Prop_ICeCliff_H.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat_AlphaTest"
                        shaderMacros: map[string,string] = {
                            "DISABLE_FOW" = "1"
                            "DISABLE_DEPTH_FOG" = "1"
                        }
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/Howling_Abyss/Materials/p_healthpack_emmit_geo_alpha_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/p_healthpack_emmit_geo_alpha_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/prop_healthpack.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/Howling_Abyss/Materials/lambert233_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/lambert233_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Structure_Base_Wall_G.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/polySurface174029_shader_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/polySurface174029_shader_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Structure_Lane_Walls2.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/lanewalls_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/lanewalls_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/structure_lane_walls.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/LM_ground_bracket_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/LM_ground_bracket_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/prop_bracket.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/ice_blocks_alpha_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/ice_blocks_alpha_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/prop_ice_chunksa.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.00499999989, 0, 0, 0 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/Howling_Abyss/Materials/BK_periph_base_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/BK_periph_base_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/structure_periph_base.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/BKDF_Matte_Skybox1_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/BKDF_Matte_Skybox1_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/HA_Skybox_01.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                        shaderMacros: map[string,string] = {
                            "DISABLE_FOW" = "1"
                        }
                    }
                }
            }
        }
    }
    "Maps/KitPieces/Howling_Abyss/Materials/LM_Cutaway1_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/LM_Cutaway1_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/structure_hole.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/CRANE_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/CRANE_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/crane3.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/hero_emblemSG2_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/hero_emblemSG2_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/prop_bridge_keystone.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/lambert3_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/lambert3_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/shopkeeper_viking_cm_v4.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/LM_Stairs_Lane_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/LM_Stairs_Lane_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Structure_Lane_Stairs.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/lambert4166_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/lambert4166_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Prop_Statue_Hero_TowerA.DDS"
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
    "Maps/KitPieces/Howling_Abyss/Materials/lambert4190_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/lambert4190_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Statue_Base.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/SB_Wall_F1_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/SB_Wall_F1_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/structure_base_wall_F.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/lambert2_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/lambert2_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/prop_chainlink.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/fj_jeremy_shop_north_ICICLES1_alpha_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/fj_jeremy_shop_north_ICICLES1_alpha_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/props_icicles_b.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/Howling_Abyss/Materials/LM_lambert4099_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/LM_lambert4099_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/structure_lane_middlehole.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/SW_ShopICE_alpha_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/SW_ShopICE_alpha_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Props_SW_Shop_Ice_Frame.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.00499999989, 0, 0, 0 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/Howling_Abyss/Materials/NE_Gate_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/NE_Gate_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Prop_NE_Base_Gate.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/lambert4104_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/lambert4104_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/HA_AP_Hero_Tower2.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/LM_SnowShelf_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/LM_SnowShelf_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/BaseSnow.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/LM_Cutaway2_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/LM_Cutaway2_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/structure_middlehole.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/periph_ice_closeup_alpha1_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/periph_ice_closeup_alpha1_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/prop_icecliff_snowtransition.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.00499999989, 0, 0, 0 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/Howling_Abyss/Materials/BK_periph_ice_cu1_inst_blend" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/BK_periph_ice_cu1_inst_blend"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Prop_ICeCliff_H.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat_AlphaTest"
                        shaderMacros: map[string,string] = {
                            "DISABLE_FOW" = "1"
                            "DISABLE_DEPTH_FOG" = "1"
                        }
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/Howling_Abyss/Materials/chain_base_plate_shader_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/chain_base_plate_shader_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Prop_chain_base_plate.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/lambert250_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/lambert250_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/prop_cloth.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/Keep_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/Keep_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Structure_Keep_A.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/NE_SHOP_Items_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/NE_SHOP_Items_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/shop_items2.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/lambert4197_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/lambert4197_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/prop_icicles_C.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/LM_polySurface172386_shader_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/LM_polySurface172386_shader_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Structure_Base_Ground.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/BK_periph_ice_cu1_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/BK_periph_ice_cu1_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Prop_ICeCliff_H.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat_AlphaTest"
                        shaderMacros: map[string,string] = {
                            "DISABLE_FOW" = "1"
                            "DISABLE_DEPTH_FOG" = "1"
                        }
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/Howling_Abyss/Materials/LM_lambert168_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/LM_lambert168_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Structure_Base_Lower_Wall.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/shouthshopice_alpha_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/shouthshopice_alpha_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/shop_keeper_magic_ice1.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.00499999989, 0, 0, 0 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/Howling_Abyss/Materials/shelves1_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/shelves1_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Shelves2.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/SHOP_CAVE_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/SHOP_CAVE_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Ice_cave_2.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/SWbase_cloth_alpha_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/SWbase_cloth_alpha_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/decal_SWbase_cloth.DDS"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/Howling_Abyss/Materials/lambert4191_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/lambert4191_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/prop_woodbeam_endcaps.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/SHOP_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/SHOP_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/structure_north_shop_comp3.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/LM_Lane3_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/LM_Lane3_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Structure_Lane_Ground.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/lambert4181_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/lambert4181_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Prop_Brazier_2.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/SB_Wall_D1_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/SB_Wall_D1_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/structure_base_wall_D.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/Statue_3_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/Statue_3_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Statue_Breakable_03.dds"
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
    "Maps/KitPieces/Howling_Abyss/Materials/BK_cliffer_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/BK_cliffer_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Prop_IceCliff_F.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                        shaderMacros: map[string,string] = {
                            "DISABLE_FOW" = "1"
                            "DISABLE_DEPTH_FOG" = "1"
                        }
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/Howling_Abyss/Materials/statue_14_breakable_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/statue_14_breakable_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Statue_Breakable_03.dds"
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
    "Maps/Particles/HA/Base/HA_Env_bridgeWind_SE_02" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.0500000007
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
                emitterName: string = "Wind"
                importance: u8 = 0
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
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
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 7, 3, 5 }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_bridgeWind_SE_02.SRE_Base.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.850000024, 0 }
                }
            }
        }
        particleName: string = "HA_Env_bridgeWind_SE_02"
        particlePath: string = "Maps/Particles/HA/Base/HA_Env_bridgeWind_SE_02"
    }
    "Maps/Particles/HA/Base/HA_Env_bridgeWind_SE_01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.0500000007
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
                emitterName: string = "Wind"
                importance: u8 = 0
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/Env_MB_bridgeWind_SE_01.sco"
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
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_bridgeWind_SE_01.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.400000006, -0.400000006 }
                }
            }
        }
        particleName: string = "HA_Env_bridgeWind_SE_01"
        particlePath: string = "Maps/Particles/HA/Base/HA_Env_bridgeWind_SE_01"
    }
    "Maps/Particles/HA/Base/HA_GemGlow_p" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                emitterName: string = "littleray"
                importance: u8 = 0
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -10, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveRay {}
                particleColorTexture: string = "ASSETS/Shared/Particles/color-RodOfAges.DDS"
                colorLookUpScales: vec2 = { 1, 0.800000012 }
                miscRenderFlags: u8 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 60, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.5, 0.5, 0.5 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/GemGlow_p.DDS"
                startFrame: u16 = 1
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "glow"
                importance: u8 = 2
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -10, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "ASSETS/Shared/Particles/color-purplehit.DDS"
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 100 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.699999988
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1.60000002, 1.60000002, 1.60000002 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/GemGlow_p.DDS"
                startFrame: u16 = 2
                texDiv: vec2 = { 2, 2 }
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                scale1: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            1
                        }
                        values: list[f32] = {
                            0
                            0.800000012
                            1.60000002
                        }
                    }
                }
                birthRotation1: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleBind: vec2 = { 1, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "sparkles"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 10, 20, -13 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -0.5
                                        0.300000012
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 10, 20, -13 }
                            }
                        }
                    }
                }
                particleColorTexture: string = "ASSETS/Shared/Particles/color-hold.TFT_Set5.dds"
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 20, 20 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/GemGlow_p.DDS"
                texDiv: vec2 = { 2, 2 }
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 20
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            20
                        }
                    }
                }
                scale1: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[f32] = {
                            0
                            1
                            0
                        }
                    }
                }
                birthRotation1: embed = ValueFloat {
                    constantValue: f32 = 45
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                emitterName: string = "Basic"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.250003815, 0.960006118, 0.480003059 }
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
                pass: i16 = 9
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1.625, 0, 0 }
                            { 20, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 50, 0 }
                }
                texture: string = "ASSETS/Shared/Particles/ball32_02.TFT_Set5.dds"
            }
        }
        particleName: string = "HA_GemGlow_p"
        particlePath: string = "Maps/Particles/HA/Base/HA_GemGlow_p"
    }
    "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big" = VfxSystemDefinitionData {
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
        particleName: string = "HA_Audio_Emitter_FireMed_Big"
        particlePath: string = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
        soundPersistentDefault: string = "Play_sfx_Env_map12_fire_med_big"
        flags: u8 = 132
    }
    "Maps/Particles/HA/Base/HA_Env_highWind_belowBridge_01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 13
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
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
                            13
                        }
                    }
                }
                emitterName: string = "Wind"
                importance: u8 = 0
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 1, 1 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -4000
                                        1000
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -4500
                                        -20000
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1000
                                        100
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 1, 1 }
                            }
                        }
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
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 54, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 25, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.29999995
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 60, 25, 50 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_highWind_01.SRE_Base.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.300000012, 0.300000012 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1.5
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
                            { 0.300000012, 0.300000012 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 2 }
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
                            { 2, 2 }
                        }
                    }
                }
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 0.100000001 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1.5
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
                            { 0.100000001, 0.100000001 }
                        }
                    }
                }
            }
        }
        visibilityRadius: f32 = 6000
        particleName: string = "HA_Env_highWind_belowBridge_01"
        particlePath: string = "Maps/Particles/HA/Base/HA_Env_highWind_belowBridge_01"
    }
    "Maps/Particles/HA/Base/HA_Env_Chimney_Smoke" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                particleLinger: option[f32] = {
                    16
                }
                lifetime: option[f32] = {
                    1000000
                }
                emitterName: string = "smoke"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 60, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -10
                                    10
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -20
                                    20
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -10
                                    10
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 2, 1, 2 }
                        }
                    }
                }
                acceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 2, 5 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                            0.75
                            1
                        }
                        values: list[vec3] = {
                            { -250, 20, 50 }
                            { 150, 2, 100 }
                            { -200, 0, 150 }
                            { 100, 0, 200 }
                            { -150, 0, 250 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { -20, 0, 10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -20, 0, 10 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "ASSETS/Shared/Particles/color-Chimney_Smoke.dds"
                blendMode: u8 = 1
                pass: i16 = 100
                colorLookUpTypeY: u8 = 3
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 60, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, -60, 0 }
                            { 0, 60, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 20, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0 }
                            { 2, 2, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_Chimney_Smoke.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "HA_Env_Chimney_Smoke"
        particlePath: string = "Maps/Particles/HA/Base/HA_Env_Chimney_Smoke"
        buildUpTime: f32 = 10
    }
    "Maps/Particles/HA/Base/HA_Audio_Emitter_Hermit_Cloth" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "sound"
                meshRenderFlags: u8 = 0
            }
        }
        visibilityRadius: f32 = 1000
        particleName: string = "HA_Audio_Emitter_Hermit_Cloth"
        particlePath: string = "Maps/Particles/HA/Base/HA_Audio_Emitter_Hermit_Cloth"
        soundPersistentDefault: string = "Play_sfx_env_map12_ha_ap_cloth"
    }
    "Maps/Particles/HA/Base/HA_Order_Inhibitor_Rubble_dust" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.699999988
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "sparkles1"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -1.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    0.200000003
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -1.5, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 0, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, -0.875, 0 }
                            { 0, -2.20000005, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 30, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 75, 0, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                        { 0, 0, 1.00000012 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.525489986, 1, 0.843137026, 0.738003016 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.525489986, 1, 0.843137026, 0 }
                            { 0.525489986, 1, 0.843137026, 0.516602099 }
                            { 0.525489986, 1, 0.843137026, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 45, 45 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.400000006
                                    0.800000012
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 45, 45, 45 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_brightSparks_teal.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
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
                                    0.800000012
                                    1.39999998
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
                    14
                }
                emitterName: string = "pitGlow"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 35, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                            { 0, 35, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 15, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 15, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -100, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 3, 3, 3 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -30
                                        30
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -30
                                        30
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -10
                                        10
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 3, 3, 3 }
                            }
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.258823991, 1, 0.811765015, 0.738003016 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.25
                            0.349999994
                            0.5
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 0.258823991, 1, 0.811765015, -0 }
                            { 0.258823991, 1, 0.811765015, 0.387451559 }
                            { 0.258823991, 1, 0.811765015, 0.571952343 }
                            { 0.258823991, 1, 0.811765015, 0.53505218 }
                            { 0.258823991, 1, 0.811765015, 0.369001508 }
                            { 0.258823991, 1, 0.811765015, 0.202950835 }
                            { 0.258823991, 1, 0.811765015, 0 }
                        }
                    }
                }
                pass: i16 = -100
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 45, 90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -90, 45, 90 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -10, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -10
                                    10
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -10, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    0.899999976
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    0.899999976
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 150, 150, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { -0, -0, 0 }
                            { 0.949999988, 0.975000024, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRUAP_ChaosTurret1_ambientGlow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.400000006
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.600000024
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
                    16
                }
                emitterName: string = "DustCloud"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 50, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 50, 1 }
                        }
                    }
                }
                velocity: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.449999988
                            1
                        }
                        values: list[vec3] = {
                            { -0, 0, 0 }
                            { -0, 0, -0 }
                            { -0, 0, -0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0.400000006
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 30, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -200, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 75, 75, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 75, 75, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.301960796, 0.517647088, 0.615686297, 0.800000072 }
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
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.301960796, 0.517647088, 0.615686297, 0.800000072 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.550000012
                            0.699999988
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.400000006 }
                            { 1, 1, 1, 0.125 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -15
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 240, 240, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                                    0.300000012
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 240, 240, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.649999976
                            1
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0.300000012, 1 }
                            { 0.5, 0.5, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_OrderTurret1_Rubble_dustCloud.dds"
                textureMult: string = "ASSETS/Shared/Particles/SRU_dustCloud_mult.dds"
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
        }
        particleName: string = "HA_Order_Inhibitor_Rubble_dust"
        particlePath: string = "Maps/Particles/HA/Base/HA_Order_Inhibitor_Rubble_dust"
        flags: u8 = 135
    }
    "Maps/Particles/HA/Base/HA_Env_Snow_01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 270
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 4000
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 2
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 50
                            }
                            axisFraction: vec3 = { 1, 1, 0 }
                        }
                    }
                }
                emitterName: string = "Snow"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -320, -200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -320, -200, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1200, 1600, 1200 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
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
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1200, 1600, 1200 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                particleColorTexture: string = "ASSETS/Shared/Particles/color-bellramp.TFT_SET4.dds"
                pass: i16 = 100
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 0 }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_snow_flakes.SRE_Base.dds"
                uvMode: u8 = 2
            }
        }
        visibilityRadius: f32 = 2000
        particleName: string = "HA_Env_Snow_01"
        particlePath: string = "Maps/Particles/HA/Base/HA_Env_Snow_01"
    }
    "Maps/Particles/HA/Base/HA_Chaos_Inhibitor_Rubble_dust" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.699999988
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "sparkles1"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -1.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    0.200000003
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -1.5, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 0, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, -0.875, 0 }
                            { 0, -2.20000005, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 30, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 75, 0, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                        { 0, 0, 1.00000012 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.525489986, 1, 0.843137026, 0.738003016 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.525489986, 1, 0.843137026, 0 }
                            { 0.525489986, 1, 0.843137026, 0.516602099 }
                            { 0.525489986, 1, 0.843137026, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 45, 45 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.400000006
                                    0.800000012
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 45, 45, 45 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_brightSparks_teal.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
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
                                    0.800000012
                                    1.39999998
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
                    14
                }
                emitterName: string = "pitGlow"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 35, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                            { 0, 35, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 15, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 15, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -100, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 3, 3, 3 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -30
                                        30
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -30
                                        30
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -10
                                        10
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 3, 3, 3 }
                            }
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.258823991, 1, 0.811765015, 0.738003016 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.25
                            0.349999994
                            0.5
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 0.258823991, 1, 0.811765015, -0 }
                            { 0.258823991, 1, 0.811765015, 0.387451559 }
                            { 0.258823991, 1, 0.811765015, 0.571952343 }
                            { 0.258823991, 1, 0.811765015, 0.53505218 }
                            { 0.258823991, 1, 0.811765015, 0.369001508 }
                            { 0.258823991, 1, 0.811765015, 0.202950835 }
                            { 0.258823991, 1, 0.811765015, 0 }
                        }
                    }
                }
                pass: i16 = -100
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 45, 90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -90, 45, 90 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -10, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -10
                                    10
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -10, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    0.899999976
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    0.899999976
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 150, 150, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { -0, -0, 0 }
                            { 0.949999988, 0.975000024, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/HA_ambientGlow_purple.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.400000006
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.600000024
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
                    16
                }
                emitterName: string = "DustCloud"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 50, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 50, 1 }
                        }
                    }
                }
                velocity: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.449999988
                            1
                        }
                        values: list[vec3] = {
                            { -0, 0, 0 }
                            { -0, 0, -0 }
                            { -0, 0, -0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0.400000006
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 30, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -200, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 75, 75, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 75, 75, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.301960796, 0.517647088, 0.615686297, 0.800000072 }
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
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.301960796, 0.517647088, 0.615686297, 0.800000072 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.550000012
                            0.699999988
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.400000006 }
                            { 1, 1, 1, 0.125 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -15
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 240, 240, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                                    0.300000012
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 240, 240, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.649999976
                            1
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0.300000012, 1 }
                            { 0.5, 0.5, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_OrderTurret1_Rubble_dustCloud.dds"
                textureMult: string = "ASSETS/Shared/Particles/SRU_dustCloud_mult.dds"
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
        }
        particleName: string = "HA_Chaos_Inhibitor_Rubble_dust"
        particlePath: string = "Maps/Particles/HA/Base/HA_Chaos_Inhibitor_Rubble_dust"
        flags: u8 = 135
    }
    "Maps/Particles/HA/Base/HA_Snow_Sparkle_01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
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
                            3
                        }
                    }
                }
                particleLinger: option[f32] = {
                    13
                }
                emitterName: string = "Basic"
                emissionMeshScale: f32 = 2
                emissionMeshName: string = "ASSETS/Shared/Particles/sru_emitter_plane.scb"
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.5
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
                    constantValue: vec4 = { 0.203922004, 0.345097989, 0.345097989, 1 }
                }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.75
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1
                                    1.54999995
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 20, 20 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/HA_Snow_Sparkle.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0500000007, 0.0500000007 }
                }
            }
        }
        particleName: string = "HA_Snow_Sparkle_01"
        particlePath: string = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
        flags: u8 = 132
    }
    "Maps/Particles/HA/Base/HA_Audio_Emitter_FireBig" = VfxSystemDefinitionData {
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
        particleName: string = "HA_Audio_Emitter_FireBig"
        particlePath: string = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireBig"
        soundPersistentDefault: string = "Play_sfx_Env_map12_fire_big"
        flags: u8 = 132
    }
    "Maps/Particles/HA/Base/HA_Audio_Emitter_Hermit_Fire" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "sound"
                meshRenderFlags: u8 = 0
            }
        }
        visibilityRadius: f32 = 1000
        particleName: string = "HA_Audio_Emitter_Hermit_Fire"
        particlePath: string = "Maps/Particles/HA/Base/HA_Audio_Emitter_Hermit_Fire"
        soundPersistentDefault: string = "Play_sfx_env_map12_ha_ap_hermitfire"
    }
    "Maps/Particles/HA/Base/HA_Order_Inhibitor_runeTimer" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 270
                }
                isSingleParticle: flag = true
                emitterName: string = "runeTimeGlow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sruap_order_inhibitor_respawn_base.scb"
                    }
                }
                blendMode: u8 = 4
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -45, 0 }
                }
                isLocalOrientation: flag = false
                texture: string = "ASSETS/Shared/Particles/SRUAP_Order_Inhibitor_RuneCountdown_glow.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00200000009, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
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
                            7
                        }
                    }
                }
                emitterName: string = "pulseTimer"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sruap_order_inhibitor_respawn_base.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.501960814 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.357143015
                            0.5
                            0.645160973
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 1, -0 }
                            { 0.699999988, 0.699999988, 1, 0.224999994 }
                            { 1, 1, 1, 1 }
                            { 0.699999988, 0.699999988, 1, 0.275000006 }
                            { 0, 0, 1, -0 }
                        }
                    }
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -45, 0 }
                }
                isLocalOrientation: flag = false
                texture: string = "ASSETS/Shared/Particles/SRUAP_Order_Inhibitor_RuneCountdown.dds"
            }
        }
        particleName: string = "HA_Order_Inhibitor_runeTimer"
        particlePath: string = "Maps/Particles/HA/Base/HA_Order_Inhibitor_runeTimer"
        flags: u8 = 133
        assetRemappingTable: list[embed] = {
            VfxAssetRemap {
                oldAsset: hash = 0x1b7b92e7
                newAsset: string = "ASSETS/Shared/Particles/SRUAP_Chaos_Inhibitor_RuneCountdown_glow.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0xf1acfd0b
                newAsset: string = "ASSETS/Shared/Particles/SRUAP_Chaos_Inhibitor_RuneCountdown.dds"
            }
        }
    }
    "Maps/Particles/HA/Base/HA_AP_godRays_01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "godRays"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { -5500, -14000, 18000 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/HA_AP_godRays_01.sco"
                    }
                }
                blendMode: u8 = 4
                pass: i16 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 6500, 6500, 6500 }
                }
                texture: string = "ASSETS/Shared/Particles/HA_AP_godRays_diff.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.00999999978, 0 }
                }
                textureMult: string = "ASSETS/Shared/Particles/HA_AP_godRays_diff.dds"
            }
        }
        visibilityRadius: f32 = 5000
        particleName: string = "HA_AP_godRays_01"
        particlePath: string = "Maps/Particles/HA/Base/HA_AP_godRays_01"
    }
    "Maps/Particles/HA/Base/HA_Chaos_Inhibitor_runeTimer" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 270
                }
                isSingleParticle: flag = true
                emitterName: string = "runeTimeGlow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sruap_order_inhibitor_respawn_base.scb"
                    }
                }
                blendMode: u8 = 4
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 135, 0 }
                }
                isLocalOrientation: flag = false
                texture: string = "ASSETS/Shared/Particles/SRUAP_Chaos_Inhibitor_RuneCountdown_glow.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00200000009, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
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
                            7
                        }
                    }
                }
                emitterName: string = "pulseTimer"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sruap_order_inhibitor_respawn_base.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.501960814 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.357143015
                            0.5
                            0.645160973
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 1, -0 }
                            { 0.699999988, 0.699999988, 1, 0.224999994 }
                            { 1, 1, 1, 1 }
                            { 0.699999988, 0.699999988, 1, 0.275000006 }
                            { 0, 0, 1, -0 }
                        }
                    }
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 135, 0 }
                }
                isLocalOrientation: flag = false
                texture: string = "ASSETS/Shared/Particles/SRUAP_Chaos_Inhibitor_RuneCountdown.dds"
            }
        }
        particleName: string = "HA_Chaos_Inhibitor_runeTimer"
        particlePath: string = "Maps/Particles/HA/Base/HA_Chaos_Inhibitor_runeTimer"
        flags: u8 = 133
        assetRemappingTable: list[embed] = {
            VfxAssetRemap {
                oldAsset: hash = 0xaa3a888f
                newAsset: string = "ASSETS/Shared/Particles/SRUAP_Order_Inhibitor_RuneCountdown_glow.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0x37d25f93
                newAsset: string = "ASSETS/Shared/Particles/SRUAP_Order_Inhibitor_RuneCountdown.dds"
            }
        }
    }
    "Maps/Particles/HA/Base/HA_Env_hightWind_01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.0500000007
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
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "Wind"
                importance: u8 = 0
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
                            { 1, 1, 1, 0.699999988 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 44, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 1, 10 }
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
                                    0.600000024
                                    0.699999988
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
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 4000
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 2
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 50
                            }
                            axisFraction: vec3 = { 1, 1, 0 }
                        }
                    }
                }
                emitterName: string = "Snow"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -1220, -150, 200 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -1220, -150, 200 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1200, 1200, 1200 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        2.5
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
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1200, 1200, 1200 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
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
                pass: i16 = 100
                isDirectionOriented: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 20, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 20, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_snow_flakes.SRE_Base.dds"
            }
        }
        visibilityRadius: f32 = 500
        particleName: string = "HA_Env_hightWind_01"
        particlePath: string = "Maps/Particles/HA/Base/HA_Env_hightWind_01"
    }
    "Maps/Particles/HA/Base/HA_Env_brazierFire_particles" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.600000024
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "Fire"
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { -700, 950, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -700, 950, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 20, 10, 20 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 20, 10, 20 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.800000012 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -180
                                    180
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 50, 50 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0.600000024, 0.600000024 }
                            { 1, 1, 1 }
                            { 0.600000024, 0.600000024, 0.600000024 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_flipbook_01.SRI_Slots.dds"
                numFrames: u16 = 8
                texDiv: vec2 = { 4, 2 }
                textureMult: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_mult.SRI_Slots.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -1.25 }
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
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
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
                texDivMult: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
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
                            1.5
                        }
                    }
                }
                emitterName: string = "baseGlow"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
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
                            { 1, 1, 1, 1 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 2
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 125, 125, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.100000001, 0.100000001, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_glow.TFT_Set4.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
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
                            0.800000012
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.8000002
                }
                emitterName: string = "sparks"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0.400000006, 0.400000006, 0.400000006 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0.400000006, 0.400000006, 0.400000006 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -250, 500, 0 }
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
                            { -250, 500, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0.600000024, 0.600000024, 0.600000024 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 25, -25, 25 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 25, -25, 25 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
                colorLookUpTypeY: u8 = 3
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 0 }
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
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 30, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0.5, 0 }
                            { 0.200000003, 0.200000003, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_Ash_01.TFT_Set4.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2.5
                        }
                    }
                }
                emitterName: string = "Smoke"
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { -80, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
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
                            { -80, 150, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 30, 30, 10 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 30, 30, 10 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 25
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 0.800000012, 0.800000012, 0.300000012 }
                            { 1, 0.600000024, 0.800000012, 0.100000001 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 80, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 80, 80, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0.200000003, 0.600000024 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazier_dust.VFX_Update_SS_Ignite.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.400000006 }
                }
                textureMult: string = "ASSETS/Shared/Particles/Env_MB_brazier_dust_mult.VFX_Update_SS_Ignite.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.25 }
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
                                    1
                                    0
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0
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
                    constantValue: f32 = 6
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.649999976
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "fireGlow"
                disabled: bool = true
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { -800, 850, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            { -800, 850, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 30, 10, 10 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 30, 10, 10 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 3
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    180
                                    -180
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 75, 75, 75 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0.600000024, 0 }
                            { 1, 1, 0 }
                            { 0.600000024, 0.600000024, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_flipbookGlow_01.dds"
                textureMult: string = "ASSETS/Shared/Particles/Env_MB_brazier_dust_mult.VFX_Update_SS_Ignite.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.25 }
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
                                    1
                                    0
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0
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
        }
        particleName: string = "HA_Env_brazierFire_particles"
        particlePath: string = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles"
    }
    "Maps/Particles/HA/Base/HA_Env_lowWind_01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.0500000007
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
                importance: u8 = 0
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 650, 1 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1000
                                        1000
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1000
                                        1000
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 650, 1 }
                            }
                        }
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
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 54, 0 }
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
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
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
                                    0.300000012
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
                    2
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 4000
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 2
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 50
                            }
                            axisFraction: vec3 = { 1, 1, 0 }
                        }
                    }
                }
                emitterName: string = "Snow"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -1020, -150, 100 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -1020, -150, 100 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1200, 1200, 1200 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1.5
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
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1200, 1200, 1200 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
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
                pass: i16 = 100
                isDirectionOriented: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 12, 18, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 12, 18, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_snow_flakes.SRE_Base.dds"
            }
        }
        visibilityRadius: f32 = 1500
        particleName: string = "HA_Env_lowWind_01"
        particlePath: string = "Maps/Particles/HA/Base/HA_Env_lowWind_01"
    }
    "Maps/Particles/HA/Base/HA_Env_brazierFire_particles_small" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            15
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
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
                            0.600000024
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "Fire"
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 800, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.300000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 800, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.25
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 10, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                    2
                                }
                                keyValues: list[f32] = {
                                    -90
                                    90
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 28, 28, 28 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0.600000024, 0.600000024 }
                            { 1, 1, 1 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_flipbook_01.SRI_Slots.dds"
                numFrames: u16 = 8
                texDiv: vec2 = { 4, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.649999976
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "fireGlow"
                disabled: bool = true
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 600, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.100000001
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 600, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 3
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    180
                                    -180
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 35, 35, 75 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0.600000024, 0 }
                            { 1, 1, 0 }
                            { 0.600000024, 0.600000024, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_flipbookGlow_01.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
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
                            1.5
                        }
                    }
                }
                emitterName: string = "baseGlow"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 2
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    100
                                    -100
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 75, 75, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.100000001, 0.100000001, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_glow.TFT_Set4.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.99000001
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                    20
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            5
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
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
                            0.600000024
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.6000004
                }
                emitterName: string = "fireash"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0.400000006, 0.400000006, 0.400000006 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0.400000006, 0.400000006, 0.400000006 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 500, 0 }
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
                        values: list[vec3] = {
                            { 0, 500, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0.600000024, 0.600000024, 0.600000024 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                }
                particleColorTexture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_colorMap.dds"
                colorLookUpTypeY: u8 = 3
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 0 }
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
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 30, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0.200000003, 0.200000003, 0 }
                            { 1, 0.5, 0 }
                            { 0.200000003, 0.200000003, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_Ash_01.TFT_Set4.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
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
                                    0.600000024
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
                emitterName: string = "Smoke"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 400, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 400, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -120, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                        }
                                        keyValues: list[f32] = {
                                            45
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 0, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                isDirectionOriented: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.39999998
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.39999998
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 50, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0.200000003, 0.600000024 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_dust_small.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                }
                textureMult: string = "ASSETS/Shared/Particles/Env_MB_dust_small_mult.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.150000006 }
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
                                    1
                                    0
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0
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
        }
        particleName: string = "HA_Env_brazierFire_particles_small"
        particlePath: string = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles_small"
    }
    "Maps/Particles/HA/Base/HA_Env_backgroundClouds_01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            8
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "Wind"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 0, 1 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 300, 0, 1 }
                        }
                    }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, -4 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 1, 1 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1000
                                        8000
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -20000
                                        -6000
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -3500
                                        3500
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 1, 1 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 240
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/Env_MB_abyssClouds_01.sco"
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
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 40, 40 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.699999988, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_abyssClouds_01.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0299999993, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.699999988
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0299999993, 0 }
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
            }
        }
        visibilityRadius: f32 = 8000
        particleName: string = "HA_Env_backgroundClouds_01"
        particlePath: string = "Maps/Particles/HA/Base/HA_Env_backgroundClouds_01"
    }
    "Maps/MapGeometry/Map12/Chunks/Default" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x2c2150c2 = MapPointLight {
                type: link = 0xdd38b4a4
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8688, 288, 9857, 1
                }
                name: string = "light_6_1"
            }
            0x9d064427 = MapPointLight {
                type: link = 0xde38b637
                radiusScale: f32 = 0.99999994
                intensityScale: f32 = 0.200000003
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11448.1855, -574, 12688.8135, 1
                }
                name: string = "light_7_1"
            }
            0xdd277332 = MapPointLight {
                type: link = 0xd338a4e6
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8967, 379, 8764, 1
                }
                name: string = "light_8_1"
            }
            0x169b9329 = MapPointLight {
                type: link = 0xd438a679
                intensityScale: f32 = 1.06666696
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    767, 475, 797, 1
                }
                name: string = "light_9_1"
            }
            0x96bcb1b6 = MapPointLight {
                type: link = 0xce41fcf3
                intensityScale: f32 = 2.4000001
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    550, 318, 508, 1
                }
                name: string = "light_10_1"
            }
            0xdfd1c3e6 = MapPointLight {
                type: link = 0xcd41fb60
                intensityScale: f32 = 3.64444399
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3954, 362, 2836, 1
                }
                name: string = "light_11_1"
            }
            0x3124bc1d = MapPointLight {
                type: link = 0xd0420019
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11008, 282, 10870, 1
                }
                name: string = "light_12_1"
            }
            0x3f33eed9 = MapPointLight {
                type: link = 0xcf41fe86
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9682, 208, 9550, 1
                }
                name: string = "light_13_1"
            }
            0xbae6acaa = MapPointLight {
                type: link = 0xd242033f
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1876, 471, 1980, 1
                }
                name: string = "light_14_1"
            }
            0x877d246c = MapPointLight {
                type: link = 0xd14201ac
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3115, 320, 3129, 1
                }
                name: string = "light_15_1"
            }
            0x39dd8c2e = MapPointLight {
                type: link = 0xd4420665
                radiusScale: f32 = 1.14540577
                intensityScale: f32 = 3.91111112
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2107.40796, 18, 4251.5542, 1
                }
                name: string = "light_16_1"
            }
            0x22843958 = MapPointLight {
                type: link = 0xd34204d2
                intensityScale: f32 = 3.82222199
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2823, 287, 4163, 1
                }
                name: string = "light_17_1"
            }
            0x73eb1a4d = MapPointLight {
                type: link = 0xd642098b
                intensityScale: f32 = 0.955555975
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7499, -406, 5111, 1
                }
                name: string = "light_18_1"
            }
            0x1719c3a4 = MapPointLight {
                type: link = 0xd34204d2
                intensityScale: f32 = 3.79999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9986, 337, 8523, 1
                }
                name: string = "light_19_1"
            }
            0x3e23681c = MapPointLight {
                type: link = 0x5c3a8db8
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2054, 369, 2599, 1
                }
                name: string = "light_20_1"
            }
            0x4913bfca = MapPointLight {
                type: link = 0x5d3a8f4b
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2577, 185, 2095, 1
                }
                name: string = "light_21_1"
            }
            0x70b56e75 = MapPointLight {
                type: link = 0x5e3a90de
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10253, 393, 10517, 1
                }
                name: string = "light_22_1"
            }
            0x705539c8 = MapPointLight {
                type: link = 0x5f3a9271
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10743, 381, 10037, 1
                }
                name: string = "light_23_1"
            }
            0x472f2ca9 = MapPointLight {
                type: link = 0x603a9404
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    366, 1916, 616, 1
                }
                name: string = "light_24_1"
            }
            0x3f5b4100 = MapPointLight {
                type: link = 0x613a9597
                intensityScale: f32 = 0.866666973
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1481, 280, 1919, 1
                }
                name: string = "light_25_1"
            }
            0x06807578 = MapPointLight {
                type: link = 0x623a972a
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12023, 82, 11746, 1
                }
                name: string = "light_26_1"
            }
            0x1bfa38eb = MapPointLight {
                type: link = 0x633a98bd
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4974, 281, 4915, 1
                }
                name: string = "light_27_1"
            }
            0x7f49fc0e = MapPointLight {
                type: link = 0x5d3a8f4b
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3799, 415, 3800, 1
                }
                name: string = "light_28_1"
            }
            0xe392a404 = MapPointLight {
                type: link = 0x553a82b3
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7775, 486, 7694, 1
                }
                name: string = "light_29_1"
            }
            0x57bfa859 = MapPointLight {
                type: link = 0x623cd5c1
                intensityScale: f32 = 2.51111102
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2116, 100, 47, 1
                }
                name: string = "light_30_1"
            }
            0xe8e5a638 = MapPointLight {
                type: link = 0x613cd42e
                intensityScale: f32 = 1.22222197
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1302, 155, 3498, 1
                }
                name: string = "light_31_1"
            }
            0x8fc4ce9e = MapPointLight {
                type: link = 0x603cd29b
                radiusScale: f32 = 0.99999994
                intensityScale: f32 = 1.17777801
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4793.83984, -71.9997559, 3929.03369, 1
                }
                name: string = "light_32_1"
            }
            0x0a2a1b1b = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 1.39267755
                intensityScale: f32 = 1.911111
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    539.940918, -7583.2666, 20599.8262, 1
                }
                name: string = "light_33_1"
            }
            0xc6ad8b39 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 4.00028515
                intensityScale: f32 = 2.71111107
                overrideCastStaticShadows: option[bool] = {
                    true
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -13502.2558, 2353.51709, 16685.582, 1
                }
                name: string = "light_33_2"
            }
            0x4cc98ac8 = MapPointLight {
                type: link = 0x603cd29b
                intensityScale: f32 = 0.977778018
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8890, -113, 7885, 1
                }
                name: string = "light_34_1"
            }
            0x86ac2bdd = MapPointLight {
                type: link = 0x603cd29b
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7579.58154, -100.999939, 6791.93359, 1
                }
                name: string = "light_34_2"
            }
            0xa4e6cb42 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5389.58594, -5036.38086, 19367.6152, 1
                }
                name: string = "light_33_3"
            }
            0x6f458228 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 2.35555601
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -885.400757, 2003.82983, 6051.31006, 1
                }
                name: string = "light_33_4"
            }
            0xa1cf7e30 = MapPointLight {
                type: link = 0x603cd29b
                radiusScale: f32 = 0.99999994
                intensityScale: f32 = 1.20000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5937.52783, -80.999939, 5183.27392, 1
                }
                name: string = "light_35_1"
            }
            0x3c658dfc = MapPointLight {
                type: link = 0x643cd8e7
                intensityScale: f32 = 3.64444399
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11052, 182, 11753, 1
                }
                name: string = "light_36_1"
            }
            0x387b8c36 = MapPointLight {
                type: link = 0x633cd754
                intensityScale: f32 = 0.955555975
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11979, 139, 12024, 1
                }
                name: string = "light_37_1"
            }
            0xbe7bbc2d = MapPointLight {
                type: link = 0x5a3cc929
                intensityScale: f32 = 3.06666708
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12196, 296, 11930, 1
                }
                name: string = "light_38_1"
            }
            0xe57577fb = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.17786562
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    724, 47, 3056, 1
                }
                name: string = "light_31_2"
            }
            0x5d0f229b = MapPointLight {
                type: link = 0xd4420665
                radiusScale: f32 = 0.836956501
                intensityScale: f32 = 3.91111112
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1815, 36, 4029, 1
                }
                name: string = "light_16_2"
            }
            0x2632fd2e = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.26482213
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1123, 48, 3462, 1
                }
                name: string = "light_31_3"
            }
            0xd772808f = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.70355725
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2265, 126, 163, 1
                }
                name: string = "light_31_4"
            }
            0x3ae4791d = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.35177863
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    75, 47, 2508, 1
                }
                name: string = "light_31_5"
            }
            0xb307760e = MapPointLight {
                type: link = 0x593cc796
                radiusScale: f32 = 0.623409271
                intensityScale: f32 = 1.31111097
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -63.7095566, 148.173599, 2118.59351, 1
                }
                name: string = "light_39_1"
            }
            0x342a2d3a = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.17786562
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    508, 39, 2836, 1
                }
                name: string = "light_31_6"
            }
            0xcd82056f = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.43873513
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2945, 152, 729, 1
                }
                name: string = "light_31_7"
            }
            0x92ec312f = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.70355725
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2744, 194, 550, 1
                }
                name: string = "light_31_8"
            }
            0x36a7b95f = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.70355725
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3568, 101, 1415, 1
                }
                name: string = "light_31_9"
            }
            0xc9f8b50a = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.70355725
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3368, 226, 1172, 1
                }
                name: string = "light_31_10"
            }
            0x906b00f0 = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.70355725
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3970, 106, 1838, 1
                }
                name: string = "light_31_11"
            }
            0x52a5df82 = MapPointLight {
                type: link = 0xd4420665
                intensityScale: f32 = 3.28888893
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1390, 123, 3618, 1
                }
                name: string = "light_31_12"
            }
            0xd038fe59 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 3.9418447
                intensityScale: f32 = 1.64444399
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7098.43262, -419.258789, 22028.0859, 1
                }
                name: string = "light_33_5"
            }
            0xa726a147 = MapPointLight {
                type: link = 0x5f3cd108
                intensityScale: f32 = 1.51111102
                overrideCastStaticShadows: option[bool] = {
                    true
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -2652, -7861, 16872, 1
                }
                name: string = "light_33_6"
            }
            0x1f6a36d6 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 32.3592148
                intensityScale: f32 = 1.20000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -3694.30127, -3454.58105, 30231.1328, 1
                }
                name: string = "light_33_7"
            }
            0xf0b2949b = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 2.33333302
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -5697.07226, -6058.22021, 14530.5947, 1
                }
                name: string = "light_33_8"
            }
            0x86c32945 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.42222202
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -1289.03906, 340.142944, 8225.63574, 1
                }
                name: string = "light_33_9"
            }
            0xb3fbdef8 = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.70355725
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4198, 166, 2014, 1
                }
                name: string = "light_31_13"
            }
            0xbb672cd7 = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 1.04999995
                intensityScale: f32 = 3.64444399
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4937, 288, 3618, 1
                }
                name: string = "light_6_2"
            }
            0x214ed74c = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 1.04431593
                intensityScale: f32 = 3.82222199
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5059, 275, 6364, 1
                }
                name: string = "light_17_2"
            }
            0xbcc27bb2 = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 1.04431593
                intensityScale: f32 = 3.82222199
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6500, 359, 7704, 1
                }
                name: string = "light_17_3"
            }
            0x161b491f = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 1.04431593
                intensityScale: f32 = 3.82222199
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7923, 422, 9117, 1
                }
                name: string = "light_17_4"
            }
            0x1d0f2689 = MapPointLight {
                type: link = 0xd34204d2
                intensityScale: f32 = 3.64444399
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6359, 332, 4991, 1
                }
                name: string = "light_40_1"
            }
            0x44b432bb = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 1.04999995
                intensityScale: f32 = 3.64444399
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7786, 503, 6326, 1
                }
                name: string = "light_6_3"
            }
            0xd3b3af29 = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 1.04431593
                intensityScale: f32 = 3.82222199
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9203, 284, 7756, 1
                }
                name: string = "light_17_5"
            }
            0xb2f0f874 = MapPointLight {
                type: link = 0x613cd42e
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8585, 25, 10742, 1
                }
                name: string = "light_31_14"
            }
            0x0aaa4c01 = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.35177863
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8836, 82, 11019, 1
                }
                name: string = "light_31_15"
            }
            0xee09028b = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.09090912
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9241, 66, 11276, 1
                }
                name: string = "light_31_16"
            }
            0xff072485 = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.09090912
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9446, 37, 11539, 1
                }
                name: string = "light_31_17"
            }
            0x9adc13d1 = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.43873513
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10111, 77, 12100, 1
                }
                name: string = "light_31_18"
            }
            0x68c6e964 = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.09090912
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9871, 71, 11876, 1
                }
                name: string = "light_31_19"
            }
            0xa668db14 = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.35177863
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11016, 18, 8593, 1
                }
                name: string = "light_31_20"
            }
            0x9634e2e0 = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.52569175
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10857, 120, 8463, 1
                }
                name: string = "light_31_21"
            }
            0x15e5b329 = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.35177863
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11487, 52, 9121, 1
                }
                name: string = "light_31_22"
            }
            0x587801b0 = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.35177863
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11622, -30, 9210, 1
                }
                name: string = "light_31_23"
            }
            0x9db9c5d1 = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.35177863
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12091, 47, 9693, 1
                }
                name: string = "light_31_24"
            }
            0xf1fe7ede = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.17786562
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12770, -7, 10288, 1
                }
                name: string = "light_31_25"
            }
            0xe77ee16a = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.35177863
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12309, 101, 9778, 1
                }
                name: string = "light_31_26"
            }
            0xfe0b67c3 = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.17786562
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12846, 98, 10383, 1
                }
                name: string = "light_31_27"
            }
            0xcaf823e2 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.26275
                intensityScale: f32 = 2.04444504
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1651, 348, 831, 1
                }
                name: string = "light_33_10"
            }
            0xe5270c9d = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.462249994
                intensityScale: f32 = 1.26666701
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1348, 443, 2420, 1
                }
                name: string = "light_33_11"
            }
            0x4cd3bd29 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.462249994
                intensityScale: f32 = 1.66666698
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2450, 448, 1297, 1
                }
                name: string = "light_33_12"
            }
            0xac57936c = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.412499875
                intensityScale: f32 = 1.79999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2192.60083, 363.601196, 3497.53418, 1
                }
                name: string = "light_33_13"
            }
            0x841298fc = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.412499994
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3305, 405, 2330, 1
                }
                name: string = "light_33_14"
            }
            0x8cb0b942 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.412499994
                intensityScale: f32 = 2.04444504
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4432, 406, 4392, 1
                }
                name: string = "light_33_15"
            }
            0x15eca93a = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.412499994
                intensityScale: f32 = 2.04444504
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5382, 509, 5353, 1
                }
                name: string = "light_33_16"
            }
            0x99b80354 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.412499994
                intensityScale: f32 = 2.04444504
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7534, 354, 7416, 1
                }
                name: string = "light_33_17"
            }
            0x38683454 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.412499934
                intensityScale: f32 = 3
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6475, 364.999939, 6345, 1
                }
                name: string = "light_33_18"
            }
            0xd2dcd8b0 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.412499994
                intensityScale: f32 = 2.26666689
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8545, 481, 8368, 1
                }
                name: string = "light_33_19"
            }
            0x937ae00b = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.412499994
                intensityScale: f32 = 2.04444504
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9428, 458, 9251, 1
                }
                name: string = "light_33_20"
            }
            0xa6489a4c = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.37924999
                intensityScale: f32 = 2.04444504
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9379, 283, 10286, 1
                }
                name: string = "light_33_21"
            }
            0xe803b52f = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.412499994
                intensityScale: f32 = 2.04444504
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10457, 284, 9191, 1
                }
                name: string = "light_33_22"
            }
            0x3c2e2c36 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.412499994
                intensityScale: f32 = 2.04444504
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11341, 254, 9723, 1
                }
                name: string = "light_33_23"
            }
            0x23dd258f = MapPointLight {
                type: link = 0x6149a021
                intensityScale: f32 = 2.04444504
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11608, 261, 11290, 1
                }
                name: string = "light_41_1"
            }
            0x60153fd4 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.412499994
                intensityScale: f32 = 2.04444504
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10043, 186, 11073, 1
                }
                name: string = "light_33_24"
            }
            0x83e000a3 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.312750012
                intensityScale: f32 = 2.04444504
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11928, 353, 10369, 1
                }
                name: string = "light_33_25"
            }
            0x20b0f027 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.412499994
                intensityScale: f32 = 2.04444504
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3663, 1555, 2296, 1
                }
                name: string = "light_33_26"
            }
            0x7fd12465 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.412499875
                intensityScale: f32 = 1.20000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3518, 379.779297, 3569, 1
                }
                name: string = "light_33_27"
            }
            0x656526ae = MapPointLight {
                type: link = 0x5e499b68
                radiusScale: f32 = 0.99999994
                intensityScale: f32 = 2.11111093
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5230.64453, -648, 2379.97754, 1
                }
                name: string = "light_42_1"
            }
            0x6c86aa8f = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.301750004
                intensityScale: f32 = 2.4222219
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5237, 334, 1425, 1
                }
                name: string = "light_33_28"
            }
            0xfbee8406 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.440250009
                intensityScale: f32 = 2.11111093
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10580, -2520, 7762, 1
                }
                name: string = "light_33_29"
            }
            0xdb17ccf5 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.412499994
                intensityScale: f32 = 1.97777796
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5515, -251, 3447, 1
                }
                name: string = "light_33_30"
            }
            0x8623c928 = MapPointLight {
                type: link = 0x5f499cfb
                intensityScale: f32 = 2.11111093
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4808, 256, 2264, 1
                }
                name: string = "light_43_1"
            }
            0x9aa2a931 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.517749965
                intensityScale: f32 = 2.86666703
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6075.09228, -2013.00098, 3348.51953, 1
                }
                name: string = "light_33_31"
            }
            0x525d8db9 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.540000021
                intensityScale: f32 = 2.4222219
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6585, 320, 1421, 1
                }
                name: string = "light_33_32"
            }
            0x703d0523 = MapPointLight {
                type: link = 0x6449a4da
                radiusScale: f32 = 0.99999994
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4742.86719, -1330.99976, 4408.89355, 1
                }
                name: string = "light_44_1"
            }
            0x631272ff = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.639750004
                intensityScale: f32 = 0.155555993
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9567, -3731, 6409, 1
                }
                name: string = "light_33_33"
            }
            0xbb192b16 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.26275
                intensityScale: f32 = 2.28888893
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10909, -4423, 6366, 1
                }
                name: string = "light_33_34"
            }
            0xb5356e03 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 2.4906733
                intensityScale: f32 = 3.04444504
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10230.2432, -9030.63867, 3679.39551, 1
                }
                name: string = "light_33_35"
            }
            0xd91f7102 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.213
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6939, -899, 4517, 1
                }
                name: string = "light_33_36"
            }
            0x90520fe1 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.412499994
                intensityScale: f32 = 2.51111102
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    14511, -2514, 5766, 1
                }
                name: string = "light_33_37"
            }
            0x5e8dd66f = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.561999977
                intensityScale: f32 = 1.95555604
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    16218, -2406.08887, 5109, 1
                }
                name: string = "light_33_38"
            }
            0xe973c454 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.412499994
                intensityScale: f32 = 1.13333297
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12952, -2417, 6784, 1
                }
                name: string = "light_33_39"
            }
            0x38e46a08 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.484499991
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12450, -1343, 5564, 1
                }
                name: string = "light_33_40"
            }
            0xe364fb5b = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.99425
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12884, -1142, 3418, 1
                }
                name: string = "light_33_41"
            }
            0x95f4502e = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.789250016
                intensityScale: f32 = 2.91111112
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    18466, -2830, 5906, 1
                }
                name: string = "light_33_42"
            }
            0x13a3a2f7 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.412499994
                intensityScale: f32 = 1.46666706
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8998, -2659, 8732, 1
                }
                name: string = "light_33_43"
            }
            0xf77cb362 = MapPointLight {
                type: link = 0x6549a66d
                intensityScale: f32 = 2.08888888
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7749, -2044, 10217, 1
                }
                name: string = "light_45_1"
            }
            0x5b29f9dd = MapPointLight {
                type: link = 0x6249a1b4
                intensityScale: f32 = 1.911111
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6117, -857, 11830, 1
                }
                name: string = "light_46_1"
            }
            0x9664c8a8 = MapPointLight {
                type: link = 0x6249a1b4
                radiusScale: f32 = 1.07104707
                intensityScale: f32 = 1.62222195
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5948, -2201, 11236, 1
                }
                name: string = "light_46_2"
            }
            0x762fcd08 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.501249969
                intensityScale: f32 = 2.04444504
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3659.78857, -2334.99854, 13651.2217, 1
                }
                name: string = "light_33_44"
            }
            0x5b106bf9 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.26275
                intensityScale: f32 = 0.644443989
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5721.00342, -1151.00049, 12800.1816, 1
                }
                name: string = "light_33_45"
            }
            0xe72afc71 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.307249993
                intensityScale: f32 = 1.37777805
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5376.20801, -1368.99951, 13621.7217, 1
                }
                name: string = "light_33_46"
            }
            0x53345841 = MapPointLight {
                type: link = 0x6349a347
                radiusScale: f32 = 0.99999994
                intensityScale: f32 = 2.28888893
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7268, -495, 12549.335, 1
                }
                name: string = "light_47_1"
            }
            0x2d08ab07 = MapPointLight {
                type: link = 0x584991f6
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 2.46666694
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6201.78662, -201.072479, 12714.1328, 1
                }
                name: string = "light_48_1"
            }
            0x0507cb1b = MapPointLight {
                type: link = 0x59499389
                intensityScale: f32 = 0.488889009
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10651, -1183, 8147, 1
                }
                name: string = "light_49_1"
            }
            0xf702c564 = MapPointLight {
                type: link = 0x664be697
                intensityScale: f32 = 1.62222195
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12631, 461, 7537, 1
                }
                name: string = "light_50_1"
            }
            0x67b1fd60 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.755999982
                intensityScale: f32 = 2.24444389
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5565, -3618, 11110, 1
                }
                name: string = "light_33_47"
            }
            0x8ed46e8d = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.501250029
                intensityScale: f32 = 0.577777982
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6644, -3806, 9678, 1
                }
                name: string = "light_33_48"
            }
            0xcfad310d = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.501250029
                intensityScale: f32 = 0.400000006
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7672, -3393, 9261, 1
                }
                name: string = "light_33_49"
            }
            0x3e475919 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.501249969
                intensityScale: f32 = 1.13333297
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5256.05273, -2244.99976, 12316.3818, 1
                }
                name: string = "light_33_50"
            }
            0x99a85bfd = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.26275
                intensityScale: f32 = 1.02222204
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6944, -591, 11990, 1
                }
                name: string = "light_33_51"
            }
            0xc52c2f36 = MapPointLight {
                type: link = 0x654be504
                intensityScale: f32 = 1.20000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11266, -1103, 7714, 1
                }
                name: string = "light_51_1"
            }
            0x78db72d4 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.440250009
                intensityScale: f32 = 0.466666996
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10181, -1471, 8545, 1
                }
                name: string = "light_33_52"
            }
            0x35b32d1f = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.401499987
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9190.83008, -1367.99976, 7215.20215, 1
                }
                name: string = "light_33_53"
            }
            0xe1aab610 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.397279948
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9751.54297, -2141.90918, 6751.28271, 1
                }
                name: string = "light_33_54"
            }
            0x6b98c09d = MapPointLight {
                type: link = 0x684be9bd
                intensityScale: f32 = 1.31111097
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    728, 67, 1289, 1
                }
                name: string = "light_52_1"
            }
            0xd6158141 = MapPointLight {
                type: link = 0x684be9bd
                intensityScale: f32 = 0.200000003
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    436, 4, 2142, 1
                }
                name: string = "light_52_2"
            }
            0xae871f95 = MapPointLight {
                type: link = 0x684be9bd
                intensityScale: f32 = 0.699999988
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    203, 164, 1438, 1
                }
                name: string = "light_52_3"
            }
            0x2a3eb81e = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.146499991
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -37.9152222, 93, 1680.4082, 1
                }
                name: string = "light_33_55"
            }
            0xc97aec8c = MapPointLight {
                type: link = 0x684be9bd
                radiusScale: f32 = 0.881205678
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    315, 105, 2433, 1
                }
                name: string = "light_52_4"
            }
            0x8dbed422 = MapPointLight {
                type: link = 0x684be9bd
                radiusScale: f32 = 0.803191483
                intensityScale: f32 = 0.400000006
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    126, 386, 2206, 1
                }
                name: string = "light_52_5"
            }
            0xdc5d45bb = MapPointLight {
                type: link = 0x684be9bd
                radiusScale: f32 = 0.960992932
                intensityScale: f32 = 0.400000006
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    659.519592, 206.000122, 2308.42676, 1
                }
                name: string = "light_52_6"
            }
            0x0cdc6273 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.2685
                intensityScale: f32 = 0.93333298
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10335, -856, 7912, 1
                }
                name: string = "light_33_56"
            }
            0xd78cce39 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.351499975
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9002.02832, -2228.33008, 6267.89551, 1
                }
                name: string = "light_33_57"
            }
            0x2ce77695 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.440250009
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11021, 1574, 7153, 1
                }
                name: string = "light_33_58"
            }
            0x98b62561 = MapPointLight {
                type: link = 0x674be82a
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11040, -344, 8135, 1
                }
                name: string = "light_53_1"
            }
            0xd01065c1 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.118749999
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9865, -2577, 8577, 1
                }
                name: string = "light_33_59"
            }
            0xdcac0b62 = MapPointLight {
                type: link = 0x6449a4da
                radiusScale: f32 = 0.99999994
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3232.38672, -2113.99976, 2479.0166, 1
                }
                name: string = "light_44_2"
            }
            0x7554061e = MapPointLight {
                type: link = 0x6449a4da
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4389, -2225, 3807, 1
                }
                name: string = "light_44_3"
            }
            0xad42cc3e = MapPointLight {
                type: link = 0x624be04b
                radiusScale: f32 = 0.99999994
                intensityScale: f32 = 0.400000006
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    176.289215, -59, 1930.66308, 1
                }
                name: string = "light_54_1"
            }
            0x16808371 = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 0.758550823
                intensityScale: f32 = 3.82222199
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6667.74609, 45.0002441, 7566.29736, 1
                }
                name: string = "light_17_6"
            }
            0x2f1b1fad = MapPointLight {
                type: link = 0x614bdeb8
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12905, 300, 10799, 1
                }
                name: string = "light_55_1"
            }
            0xa488b382 = MapPointLight {
                type: link = 0x644be371
                intensityScale: f32 = 0.200000003
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11096, -620, 12387, 1
                }
                name: string = "light_56_1"
            }
            0x29f2e1db = MapPointLight {
                type: link = 0x634be1de
                intensityScale: f32 = 0.200000003
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10943, -572, 12561, 1
                }
                name: string = "light_57_1"
            }
            0x37aea010 = MapPointLight {
                type: link = 0x634be1de
                radiusScale: f32 = 0.930158734
                intensityScale: f32 = 0.200000003
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11021, -770, 12389, 1
                }
                name: string = "light_57_2"
            }
            0xd9d0721f = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 0.915221572
                intensityScale: f32 = 3.82222199
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8111, 145, 8852, 1
                }
                name: string = "light_17_7"
            }
            0x0ec6bbd7 = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 1.04431593
                intensityScale: f32 = 3.82222199
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3663, 1544, 4823, 1
                }
                name: string = "light_17_8"
            }
            0x6cdf3e7c = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 1.04431593
                intensityScale: f32 = 3.82222199
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3623, 259, 4989, 1
                }
                name: string = "light_17_9"
            }
            0x333ed0bd = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.140999988
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    434.10437, -348.512207, 5016.15186, 1
                }
                name: string = "light_33_60"
            }
            0xb5f04597 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.163000003
                intensityScale: f32 = 2.77777791
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7779, -373, 5484, 1
                }
                name: string = "light_33_61"
            }
            0x20de9e42 = MapPointLight {
                type: link = 0x5e4bd9ff
                radiusScale: f32 = 0.99999994
                intensityScale: f32 = 2.08888888
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8457, -1234.5907, 10832, 1
                }
                name: string = "light_58_1"
            }
            0xde9c70a9 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.135499999
                intensityScale: f32 = 1.15555596
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    451, 6, 1350, 1
                }
                name: string = "light_33_62"
            }
            0xb593161b = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.684000015
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10888, -2727, 5618, 1
                }
                name: string = "light_33_63"
            }
            0x31c92dce = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.24075
                intensityScale: f32 = 0.977778018
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10307, -2914, 6424, 1
                }
                name: string = "light_33_64"
            }
            0x0963fa48 = MapPointLight {
                type: link = 0x633cd754
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12372, 195, 11759, 1
                }
                name: string = "light_37_2"
            }
            0x2267f093 = MapPointLight {
                type: link = 0xd642098b
                intensityScale: f32 = 1.31111097
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9183, 102, 6485, 1
                }
                name: string = "light_18_2"
            }
            0xd15d2276 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.440250009
                intensityScale: f32 = 1.48888898
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9825, -544, 6200, 1
                }
                name: string = "light_33_65"
            }
            0x7ad616d4 = MapPointLight {
                type: link = 0x5f3cd108
                radiusScale: f32 = 0.49000001
                intensityScale: f32 = 3.5777781
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6662, -2471, 10083, 1
                }
                name: string = "light_33_66"
            }
            0x058c785b = MapPointLight {
                type: link = 0x5d4bd86c
                intensityScale: f32 = 3.82222199
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5304, -413, 7453, 1
                }
                name: string = "light_59_1"
            }
            0x4377b137 = MapPointLight {
                type: link = 0xd44444fc
                intensityScale: f32 = 1.26666701
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11007, 498, 12270, 1
                }
                name: string = "light_60_1"
            }
            0x303b30c2 = MapPointLight {
                type: link = 0x6249a1b4
                radiusScale: f32 = 1.10630345
                intensityScale: f32 = 2.95555496
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6760, -941, 9991, 1
                }
                name: string = "light_46_3"
            }
            0x0adecf78 = MapPointLight {
                type: link = 0xd544468f
                intensityScale: f32 = 0.200000003
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11461, -426, 12450, 1
                }
                name: string = "light_61_1"
            }
            0xb486aeaf = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.17786562
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10405, 196, 12172, 1
                }
                name: string = "light_31_28"
            }
            0x353a6729 = MapPointLight {
                type: link = 0xd6444822
                intensityScale: f32 = 2.4000001
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    13058, 284, 10695, 1
                }
                name: string = "light_62_1"
            }
            0x3e175765 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_bridgeWind_SE_02"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3134.8501, -194.184998, 3161.78003, 1
                }
                name: string = "Env_MB_bridgeWind_SE_02_1"
            }
            0x9243e8e6 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_bridgeWind_SE_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3330.90991, -194.184998, 4143.27002, 1
                }
                name: string = "Env_MB_bridgeWind_SE_01_1"
            }
            0x6ecbb524 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_bridgeWind_SE_02"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3869.03003, -194.184998, 4512, 1
                }
                name: string = "Env_MB_bridgeWind_SE_02_2"
            }
            0x6dfb5ebe = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_bridgeWind_SE_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4869.1001, -191.052994, 5439.33984, 1
                }
                name: string = "Env_MB_bridgeWind_SE_01_2"
            }
            0x2be1eb3f = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_bridgeWind_SE_02"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5045.22998, -205.748993, 4762.70996, 1
                }
                name: string = "Env_MB_bridgeWind_SE_02_3"
            }
            0x22987507 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_bridgeWind_SE_02"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6643.16992, -192.154999, 7051.04004, 1
                }
                name: string = "Env_MB_bridgeWind_SE_02_4"
            }
            0xcbc77271 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_bridgeWind_SE_02"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6066.16992, -194.817001, 6193.99023, 1
                }
                name: string = "Env_MB_bridgeWind_SE_02_5"
            }
            0x4f0d0cc6 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_bridgeWind_SE_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6161.33008, -192.154999, 6368.66992, 1
                }
                name: string = "Env_MB_bridgeWind_SE_01_3"
            }
            0x23318eb3 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_bridgeWind_SE_02"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7028.77002, -192.156006, 7230.93018, 1
                }
                name: string = "Env_MB_bridgeWind_SE_02_6"
            }
            0x7e9b48cd = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_bridgeWind_SE_02"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7963.47021, -192.156006, 7650.64014, 1
                }
                name: string = "Env_MB_bridgeWind_SE_02_7"
            }
            0xe381451c = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_bridgeWind_SE_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9059.59961, -194.184998, 8561.2002, 1
                }
                name: string = "Env_MB_bridgeWind_SE_01_4"
            }
            0x1ec60b7c = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_bridgeWind_SE_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9550.05957, -192.550995, 10918.4004, 1
                }
                name: string = "Env_MB_bridgeWind_SE_01_5"
            }
            0x2c00a0d3 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_bridgeWind_SE_02"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9736.38965, -193.266998, 9432.11035, 1
                }
                name: string = "Env_MB_bridgeWind_SE_02_8"
            }
            0xef1a6402 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_bridgeWind_SE_02"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11839.7002, -191.710999, 10624.5, 1
                }
                name: string = "Env_MB_bridgeWind_SE_02_9"
            }
            0x53d3602a = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2824.6499, 149.154007, 4178.64014, 1
                }
                name: string = "Env_MB_brazierFire_particles1"
            }
            0x0e13f618 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4916.87012, 221.470001, 3617.63989, 1
                }
                name: string = "Env_MB_brazierFire_particles2"
            }
            0x1e67ee7b = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4113.06006, 140.815994, 2844.87988, 1
                }
                name: string = "Env_MB_brazierFire_particles3"
            }
            0x25f63c81 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3625.77002, 201.166, 4993.10986, 1
                }
                name: string = "Env_MB_brazierFire_particles4"
            }
            0xe7e0270f = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_hightWind_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4089.3999, -194.184998, 3326.65991, 1
                }
                name: string = "Env_MB_hightWind_01_1"
            }
            0xd006a104 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_hightWind_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3128.70996, -192.115005, 3550.04004, 1
                }
                name: string = "Env_MB_hightWind_01_2"
            }
            0x5c24511e = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_hightWind_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5302, -192.156006, 5566.87012, 1
                }
                name: string = "Env_MB_hightWind_01_3"
            }
            0xbe9dad99 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_hightWind_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5646.9502, -192.156006, 4792, 1
                }
                name: string = "Env_MB_hightWind_01_4"
            }
            0x2971b055 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_hightWind_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4158.58984, -192.154999, 5912.5, 1
                }
                name: string = "Env_MB_hightWind_01_5"
            }
            0xe8c51c51 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_hightWind_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4720.62012, -192.156006, 4592.1499, 1
                }
                name: string = "Env_MB_hightWind_01_6"
            }
            0x2e20fa84 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_hightWind_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7259.81006, -192.156006, 6495.08008, 1
                }
                name: string = "Env_MB_hightWind_01_7"
            }
            0xfacc0306 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_hightWind_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6971.52002, -192.156006, 6615.06982, 1
                }
                name: string = "Env_MB_hightWind_01_8"
            }
            0xc3ab877f = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_hightWind_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6839.12988, -318.10199, 5951.54004, 1
                }
                name: string = "Env_MB_hightWind_01_9"
            }
            0x5f41746b = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_hightWind_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9414.61035, -193.729004, 8167.52978, 1
                }
                name: string = "Env_MB_hightWind_01_10"
            }
            0xd3938337 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_hightWind_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8790.36035, -194.184998, 8950.94043, 1
                }
                name: string = "Env_MB_hightWind_01_11"
            }
            0x03505b70 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_hightWind_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9071.48047, -193.098007, 10253.5, 1
                }
                name: string = "Env_MB_hightWind_01_12"
            }
            0xd0969c2f = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_hightWind_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4794.27002, -192.156006, 5858.97998, 1
                }
                name: string = "Env_MB_hightWind_01_13"
            }
            0x76b548f5 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_hightWind_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4009.29004, -167.429001, 3068.09009, 1
                }
                name: string = "Env_MB_hightWind_01_14"
            }
            0xd75426da = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_hightWind_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7413.74023, -179.179001, 8196.66992, 1
                }
                name: string = "Env_MB_hightWind_01_15"
            }
            0xac0bd04a = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_hightWind_01"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8730.83008, -105.931, 9521.53027, 1
                }
                name: string = "Env_MB_hightWind_01_16"
            }
            0xdb6b44c9 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_Snow_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1396.12, -182.373993, 1569.59998, 1
                }
                name: string = "Env_MB_Snow_01_1"
            }
            0xcfaf5372 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_Snow_01"
                groupName: string = "snow"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11110.2002, -180.682999, 10213.4004, 1
                }
                name: string = "Env_MB_Snow_01_2"
            }
            0x9b2a4a22 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_bridgeWind_SE_02"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4307.41992, -192.154999, 4966.66016, 1
                }
                name: string = "Env_MB_bridgeWind_SE_02_10"
            }
            0x0ced7484 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_bridgeWind_SE_02"
                groupName: string = "highWinds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8020.7998, -180.876007, 8348.98047, 1
                }
                name: string = "Env_MB_bridgeWind_SE_02_11"
            }
            0x82844c06 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5054.1001, 219.792007, 6362.45996, 1
                }
                name: string = "Env_MB_brazierFire_particles5"
            }
            0xaae19022 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6348.04004, 204.886993, 4983.41016, 1
                }
                name: string = "Env_MB_brazierFire_particles6"
            }
            0x820ea52f = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6487.75976, 208.623993, 7749.25976, 1
                }
                name: string = "Env_MB_brazierFire_particles7"
            }
            0x4046aedf = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7778.39014, 209.244003, 6363.25, 1
                }
                name: string = "Env_MB_brazierFire_particles8"
            }
            0x64d8cbd5 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9203.25, 210.365997, 7743.66016, 1
                }
                name: string = "Env_MB_brazierFire_particles9"
            }
            0xbbfc6615 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7912.68018, 210.561005, 9124.9502, 1
                }
                name: string = "Env_MB_brazierFire_particles10"
            }
            0x7e4d85e1 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8681.87988, 135.906006, 9848.58008, 1
                }
                name: string = "Env_MB_brazierFire_particles11"
            }
            0x8b403bb3 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9988.5, 159.589005, 8521.88965, 1
                }
                name: string = "Env_MB_brazierFire_particles12"
            }
            0x57f73cfb = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_GemGlow_p"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12280, 383.321014, 11998, 1
                }
                name: string = "GemGlow_p1"
            }
            0x12ec7eb9 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_Snow_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11462, -132.427994, 11258.5, 1
                }
                name: string = "Env_MB_Snow_01_3"
            }
            0x435f6808 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_Snow_01"
                groupName: string = "snow"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11065.7002, -56.9813995, 5322.1001, 1
                }
                name: string = "Env_MB_Snow_01_4"
            }
            0x14b88678 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles_small"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    625.815002, -12.7741003, 2944.02002, 1
                }
                name: string = "Env_MB_brazierFire_particles_small1"
            }
            0xc7073a4c = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles_small"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1258.01001, -19.4060001, 3572.72998, 1
                }
                name: string = "Env_MB_brazierFire_particles_small2"
            }
            0xa0be0888 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles_small"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3461.3501, 25.1033993, 1272.13, 1
                }
                name: string = "Env_MB_brazierFire_particles_small3"
            }
            0x286e3a21 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles_small"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2843.76001, 9.73873043, 652.27002, 1
                }
                name: string = "Env_MB_brazierFire_particles_small4"
            }
            0x6e2f4a64 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles_small"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4091.1001, 14.2584, 1902.93005, 1
                }
                name: string = "Env_MB_brazierFire_particles_small5"
            }
            0xcb5c56a2 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles_small"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8718.73047, -1.77810001, 10792.7002, 1
                }
                name: string = "Env_MB_brazierFire_particles_small6"
            }
            0x4979be47 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles_small"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9339.95996, -23.3202991, 11404.5, 1
                }
                name: string = "Env_MB_brazierFire_particles_small7"
            }
            0xaf2889a2 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles_small"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9987.92969, -8.66884995, 12014, 1
                }
                name: string = "Env_MB_brazierFire_particles_small8"
            }
            0x988b0414 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles_small"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10926.7002, 32.4380989, 8502.07031, 1
                }
                name: string = "Env_MB_brazierFire_particles_small9"
            }
            0x591319ed = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles_small"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11565.2002, 2.93796992, 9117.50976, 1
                }
                name: string = "Env_MB_brazierFire_particles_small10"
            }
            0x2684372c = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles_small"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12215.7998, 12.6188002, 9735.42969, 1
                }
                name: string = "Env_MB_brazierFire_particles_small11"
            }
            0xe2491d3d = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles_small"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12817.2002, -3.79910994, 10342.5, 1
                }
                name: string = "Env_MB_brazierFire_particles_small12"
            }
            0x911aae69 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles_small"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2237.40991, 18.5041008, 69.168602, 1
                }
                name: string = "Env_MB_brazierFire_particles_small13"
            }
            0x65267685 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_brazierFire_particles_small"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1886.81995, -14.7090998, 4186.97021, 1
                }
                name: string = "Env_MB_brazierFire_particles_small14"
            }
            0xe3485ac7 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_Chimney_Smoke"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10867.0996, 473.735992, 12026.7998, 1
                }
                name: string = "Env_Chimney_Smoke1"
            }
            0x4d315653 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_highWind_belowBridge_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7432.68018, -192.475998, 5533.08008, 1
                }
                name: string = "Env_MB_highWind_belowBridge_01_1"
            }
            0x84cea337 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_lowWind_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9519.91016, -131.681, 8300.42969, 1
                }
                name: string = "Env_MB_lowWind_01_1"
            }
            0x734b01b6 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_lowWind_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4599.06006, -183.005997, 3588.23999, 1
                }
                name: string = "Env_MB_lowWind_01_2"
            }
            0xc2c331a5 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_lowWind_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6939.66992, -134.238998, 5840.7002, 1
                }
                name: string = "Env_MB_lowWind_01_3"
            }
            0x36afcc38 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_Snow_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6268.02002, -34977.8008, -402.628998, 1
                }
                name: string = "Env_MB_Snow_01_5"
            }
            0xdc6a15f1 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Env_backgroundClouds_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1452.07996, -182.373993, 11793.2998, 1
                }
                name: string = "Env_MB_backgroundClouds_01_1"
            }
            0xe4763103 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_AP_godRays_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -294.790985, -26.4097996, 13755.0996, 1
                }
                name: string = "HA_AP_godRays_01_1"
            }
            0xa67b222f = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_Hermit_Fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10883, 24.3554001, 11802.9004, 1
                }
                name: string = "Audio-Emitter_map12_Hermit_Fire1"
            }
            0x62e4ad66 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_Hermit_Cloth"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10688.7998, 17.1805, 11776.0996, 1
                }
                name: string = "Audio-Emitter_map12_Hermit_Cloth1"
            }
            0xd17e402f = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireBig"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9961.75, -135.102005, 8586.23047, 1
                }
                name: string = "Audio-Emitter_map12_FireBig1"
            }
            0x44160933 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireBig"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9167.9502, -27.6739006, 7730.81006, 1
                }
                name: string = "Audio-Emitter_map12_FireBig2"
            }
            0x5cf113cb = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireBig"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7744.1499, 71.0470963, 6349.68018, 1
                }
                name: string = "Audio-Emitter_map12_FireBig3"
            }
            0x8a6af8f3 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireBig"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6322.4502, 59.6874008, 4984.72998, 1
                }
                name: string = "Audio-Emitter_map12_FireBig4"
            }
            0x5e873bbd = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireBig"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4108.75976, -101.619003, 2844.86011, 1
                }
                name: string = "Audio-Emitter_map12_FireBig5"
            }
            0x8775ac6d = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4909.87988, -2.95916009, 3608.41992, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big1"
            }
            0x003653f8 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9974.57031, 73.9424973, 12021, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big2"
            }
            0x14b8dda8 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9348.29004, 120.635002, 11364.5996, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big3"
            }
            0x8016e779 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8728.40039, 61.5960999, 10807.5996, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big4"
            }
            0x27f81f5e = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10932.7002, 114.456001, 8478.2998, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big5"
            }
            0x1fbc3bd7 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12209.4004, 194.315002, 9679.99023, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big6"
            }
            0x58a06593 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12791.0996, 190.910004, 10285, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big7"
            }
            0x33f83732 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11568.9004, 131.582001, 9074.67969, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big8"
            }
            0x304f4e31 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8705.48047, 228.093994, 9813.38965, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big9"
            }
            0x8abd306e = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7946.29004, 171.442001, 9090.66992, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big10"
            }
            0x6b55fd4a = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6497.5498, 129.779007, 7751.8501, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big11"
            }
            0xf9d03776 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2820.5, 6.7425499, 4180.14014, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big12"
            }
            0x55b7d9aa = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3633.78003, 34.6055984, 4994.18018, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big13"
            }
            0x23dc207b = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    612.34198, -203.677002, 2963.63989, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big14"
            }
            0x36862a98 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1875.19995, -170.477005, 4191.31006, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big15"
            }
            0x9b4b0d23 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2014.21997, 1584.04004, 3266.82007, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big16"
            }
            0x1d986659 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1255.16003, -99.3554993, 3566.1001, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big17"
            }
            0xc9adaad5 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5051.91016, 14.6492996, 6374.02002, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big18"
            }
            0x40f91edf = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2222.27002, 106.209999, 152.089005, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big19"
            }
            0x66a348d2 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4087.02002, -175.634995, 1885.84998, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big20"
            }
            0x74b13fe5 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2824.46997, -94.0737, 629.804993, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big21"
            }
            0x28454d21 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3445.33008, -19.9501991, 1210.23999, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big22"
            }
            0xe79cc486 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3916.20996, -182.059006, 4840.0498, 1
                }
                name: string = "HA_Snow_Sparkle_01_1"
            }
            0xcb6c7ac9 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3138.15991, -182.059006, 4160.6001, 1
                }
                name: string = "HA_Snow_Sparkle_01_2"
            }
            0x93d1f197 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2479.72998, -182.731003, 4076.42993, 1
                }
                name: string = "HA_Snow_Sparkle_01_3"
            }
            0xea1ddca6 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6567.06006, -171.404999, 6383.83008, 1
                }
                name: string = "HA_Snow_Sparkle_01_4"
            }
            0xf39c0751 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    872.700989, -135.084, 2960.03003, 1
                }
                name: string = "HA_Snow_Sparkle_01_5"
            }
            0x2a3e4346 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5742.83008, -184.854996, 6267.16016, 1
                }
                name: string = "HA_Snow_Sparkle_01_6"
            }
            0x417dad97 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1991.37, -179.134995, 4069.13989, 1
                }
                name: string = "HA_Snow_Sparkle_01_7"
            }
            0x501a5576 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8007.14014, -178.078003, 8861.28027, 1
                }
                name: string = "HA_Snow_Sparkle_01_8"
            }
            0xfcdc8197 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7472.68018, -168.639999, 8336.26953, 1
                }
                name: string = "HA_Snow_Sparkle_01_9"
            }
            0xd731a469 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6503.35986, -185.380005, 6860.58984, 1
                }
                name: string = "HA_Snow_Sparkle_01_10"
            }
            0x68c9822d = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8730.16992, -179.412003, 9484.45996, 1
                }
                name: string = "HA_Snow_Sparkle_01_11"
            }
            0x14d2fde3 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8894.16992, -185.100006, 10610.7998, 1
                }
                name: string = "HA_Snow_Sparkle_01_12"
            }
            0x6bbed524 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8903.37012, -179.363007, 10207.2998, 1
                }
                name: string = "HA_Snow_Sparkle_01_13"
            }
            0xe50e68be = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10643.2002, -176.718002, 8673.33008, 1
                }
                name: string = "HA_Snow_Sparkle_01_14"
            }
            0x69d3837a = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6673.33008, -174.917007, 7531.70996, 1
                }
                name: string = "HA_Snow_Sparkle_01_15"
            }
            0x42816dfa = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6145.18994, -179.559998, 6088.41992, 1
                }
                name: string = "HA_Snow_Sparkle_01_16"
            }
            0x9b877fa6 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10266.7002, -171.417999, 8668.08008, 1
                }
                name: string = "HA_Snow_Sparkle_01_17"
            }
            0xb58b7874 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5136.33008, -181.087006, 6185.68994, 1
                }
                name: string = "HA_Snow_Sparkle_01_18"
            }
            0x340dfc8d = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6201.68018, -178.341003, 6488.22998, 1
                }
                name: string = "HA_Snow_Sparkle_01_19"
            }
            0x7f794459 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4434.16992, -182.059006, 5507.25, 1
                }
                name: string = "HA_Snow_Sparkle_01_20"
            }
            0xe8907a1b = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1493.40002, -174.953995, 275.079987, 1
                }
                name: string = "HA_Snow_Sparkle_01_21"
            }
            0xe79b83de = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2251.81006, -187.552002, 471.462006, 1
                }
                name: string = "HA_Snow_Sparkle_01_22"
            }
            0x27db70c9 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3926.17993, -182.397003, 2082.72998, 1
                }
                name: string = "HA_Snow_Sparkle_01_23"
            }
            0x97e0dbf0 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3322.92993, -179.807999, 1649.57996, 1
                }
                name: string = "HA_Snow_Sparkle_01_24"
            }
            0x474fab90 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9934.11035, -179.763, 10656.4004, 1
                }
                name: string = "HA_Snow_Sparkle_01_25"
            }
            0xc53e670b = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9798.25976, -179.781006, 11616.5, 1
                }
                name: string = "HA_Snow_Sparkle_01_26"
            }
            0x64992716 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1436.97998, -171.225998, 2324.91992, 1
                }
                name: string = "HA_Snow_Sparkle_01_27"
            }
            0x1b4995bc = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1089.25, -81.4196014, 623.630981, 1
                }
                name: string = "HA_Snow_Sparkle_01_28"
            }
            0x1109b30a = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2219.29004, -167.576004, 1557.88, 1
                }
                name: string = "HA_Snow_Sparkle_01_29"
            }
            0xd4447c99 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3907.82007, -175.802002, 2602.03003, 1
                }
                name: string = "HA_Snow_Sparkle_01_30"
            }
            0x70bd95d2 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4122.56006, -180.634995, 3922.97998, 1
                }
                name: string = "HA_Snow_Sparkle_01_31"
            }
            0x9a52bf66 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3386.84009, -153.919998, 4389.08984, 1
                }
                name: string = "HA_Snow_Sparkle_01_32"
            }
            0x4d7c985a = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3346.69995, -156.210007, 3247.03003, 1
                }
                name: string = "HA_Snow_Sparkle_01_33"
            }
            0x972c875b = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11412.2002, -179.292007, 10293, 1
                }
                name: string = "HA_Snow_Sparkle_01_34"
            }
            0xff8dde6e = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12429.9004, -189.973999, 10276.7002, 1
                }
                name: string = "HA_Snow_Sparkle_01_35"
            }
            0x1aa03383 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12209.0996, -122.528999, 11991.0996, 1
                }
                name: string = "HA_Snow_Sparkle_01_36"
            }
            0xbe68337f = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12302.7002, -184.740997, 11283.2998, 1
                }
                name: string = "HA_Snow_Sparkle_01_37"
            }
            0xb6c49d05 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12597.4004, -190.654999, 10659.7002, 1
                }
                name: string = "HA_Snow_Sparkle_01_38"
            }
            0xf6b9d532 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11216, -190.606995, 9292.00976, 1
                }
                name: string = "HA_Snow_Sparkle_01_39"
            }
            0x6a06ed84 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8184.77002, -179.595001, 7852.16016, 1
                }
                name: string = "HA_Snow_Sparkle_01_40"
            }
            0x06934acf = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4369.3501, -181.076004, 3382.23999, 1
                }
                name: string = "HA_Snow_Sparkle_01_41"
            }
            0x02395008 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1297.03003, -192.548996, 3352.73999, 1
                }
                name: string = "HA_Snow_Sparkle_01_42"
            }
            0x78d73033 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1478.26001, -144.582993, 1016.01001, 1
                }
                name: string = "HA_Snow_Sparkle_01_43"
            }
            0x681a769f = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    259.679993, -14.0862999, 805.838013, 1
                }
                name: string = "HA_Snow_Sparkle_01_44"
            }
            0x05bdc471 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8970.7998, -184.912994, 8616.92969, 1
                }
                name: string = "HA_Snow_Sparkle_01_45"
            }
            0x39f5f449 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9470.0498, -118.191002, 8299.54004, 1
                }
                name: string = "HA_Snow_Sparkle_01_46"
            }
            0xbe760dfc = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Snow_Sparkle_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3658.21997, -182.059006, 4703.81006, 1
                }
                name: string = "HA_Snow_Sparkle_01_47"
            }
            0x5435692b = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Chaos_Inhibitor_runeTimer"
                groupName: string = "RUNETIMER_CHAOS"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9689.87988, -190.740005, 9516.04004, 1
                }
                name: string = "HA_Chaos_Inhibitor_runeTimer1"
            }
            0xcc073d67 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Chaos_Inhibitor_Rubble_dust"
                groupName: string = "RUNETIMER_CHAOS"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9689.87988, -190.740005, 9516.04004, 1
                }
                name: string = "HA_Chaos_Inhibitor_Rubble_dust1"
            }
            0x8aab5b92 = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Order_Inhibitor_runeTimer"
                groupName: string = "RUNETIMER_ORDER"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3099.44995, -199.671005, 3194.15991, 1
                }
                name: string = "HA_Order_Inhibitor_runeTimer1"
            }
            0x32042c1e = MapParticle {
                system: link = "Maps/Particles/HA/Base/HA_Order_Inhibitor_Rubble_dust"
                groupName: string = "RUNETIMER_ORDER"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3099.44995, -199.671005, 3194.15991, 1
                }
                name: string = "HA_Order_Inhibitor_Rubble_dust1"
            }
            0xbf635866 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4036.00562, -193.307343, 4962.00537 }
                boxMax: vec3 = { 4171.99463, 54.3355103, 5097.99463 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4104, -193, 5030, 1
                }
                name: string = "LevelProp_brush_HA_F29"
            }
            0xa0f91e86 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7767.53808, -193, 8599.53808 }
                boxMax: vec3 = { 7922.46191, 83.571228, 8754.46191 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.853246987, 0, 0, 0
                    0, 0.853246987, 0, 0
                    0, 0, 0.853246987, 0
                    7845, -193, 8677, 1
                }
                name: string = "LevelProp_brush_HA_C36"
            }
            0x0edfd18d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5301.74854, -197.79007, 6183.74854 }
                boxMax: vec3 = { 5452.25146, 0.0973052979, 6334.25146 }
                0xad304db5: string = "Characters/brush_HA_B/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5377, -193, 6259, 1
                }
                name: string = "LevelProp_brush_HA_B24"
            }
            0x957a7a3f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6479.21533, -200, 7057.21533 }
                boxMax: vec3 = { 6660.78467, 124.139709, 7238.78467 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6570, -200, 7148, 1
                }
                name: string = "LevelProp_brush_HA_C42"
            }
            0xf8889f7d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6386.99658, -193.253143, 7261.99658 }
                boxMax: vec3 = { 6499.00342, 10.7164001, 7374.00342 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.823643982, 0, 0, 0
                    0, 0.823643982, 0, 0
                    0, 0, 0.823643982, 0
                    6443, -193, 7318, 1
                }
                name: string = "LevelProp_brush_HA_F49"
            }
            0xd3a79225 = GdsMapObject {
                type: u8 = 9
                boxMin: vec3 = { 7543.98193, -275.068085, 6746.98193 }
                boxMax: vec3 = { 7620.01807, -193, 6823.01807 }
                0xad304db5: string = "Characters/SightWard/Skins/Skin0"
                sceneLayer: string = "Info Points"
                transform: mtx44 = {
                    0.829382002, 0, 0, 0
                    0, -0.829382002, -1.01570004e-16, 0
                    0, 1.01570004e-16, -0.829382002, 0
                    7582, -193, 6785, 1
                }
                name: string = "Info_HealthPack04"
            }
            0x15929c82 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7553.82031, -193.831894, 8412.82031 }
                boxMax: vec3 = { 7700.17969, 54.0578003, 8559.17969 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.849434972, 0, 0, 0
                    0, 0.849434972, 0, 0
                    0, 0, 0.849434972, 0
                    7627, -193, 8486, 1
                }
                name: string = "LevelProp_brush_HA_A40"
            }
            0x00675d9c = GdsMapObject {
                type: u8 = 4
                boxMin: vec3 = { 1493.71167, -997.324402, 1608.45715 }
                boxMax: vec3 = { 2240.50293, 172.48587, 2355.24854 }
                0xad304db5: string = "Characters/OrderNexus/Skins/Skin1"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.970295727, 0, 0.241921872, 0
                    0, 1, 0, 0
                    -0.241921872, 0, 0.970295727, 0
                    1867, -180, 1981, 1
                }
                name: string = "HQ_T1"
            }
            0x9a39c29d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6268.73047, -208.378571, 6688.73047 }
                boxMax: vec3 = { 6355.26953, -97.0535812, 6775.26953 }
                0xad304db5: string = "Characters/brush_HA_I/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.815438986, 0, 0, 0
                    0, 0.815438986, 0, 0
                    0, 0, 0.815438986, 0
                    6312, -193, 6732, 1
                }
                name: string = "LevelProp_brush_HA_I32"
            }
            0x0cd6f6fb = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7812.93701, -218.859253, 8496.93652 }
                boxMax: vec3 = { 7919.06299, -82.3377075, 8603.06348 }
                0xad304db5: string = "Characters/brush_HA_I/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7866, -200, 8550, 1
                }
                name: string = "LevelProp_brush_HA_I26"
            }
            0xc4000299 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7804.63672, -193, 8563.63672 }
                boxMax: vec3 = { 7947.36328, 92.2662048, 8706.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7876, -193, 8635, 1
                }
                name: string = "LevelProp_brush_HA_D38"
            }
            0x43b584a9 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5916.29394, -193, 6410.29394 }
                boxMax: vec3 = { 6065.70605, 79.0877991, 6559.70605 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5991, -193, 6485, 1
                }
                name: string = "LevelProp_brush_HA_E34"
            }
            0x6d9617c7 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7694.74854, -197.79007, 8594.74805 }
                boxMax: vec3 = { 7845.25146, 0.0973052979, 8745.25195 }
                0xad304db5: string = "Characters/brush_HA_B/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7770, -193, 8670, 1
                }
                name: string = "LevelProp_brush_HA_B31"
            }
            0x55ffce73 = GdsMapObject {
                type: u8 = 9
                boxMin: vec3 = { 3112.98193, -347.068085, 1379.98206 }
                boxMax: vec3 = { 3189.01807, -265, 1456.01794 }
                0xad304db5: string = "Characters/SightWard/Skins/Skin0"
                sceneLayer: string = "Info Points"
                transform: mtx44 = {
                    0.829382002, 0, 0, 0
                    0, -0.829382002, -1.01570004e-16, 0
                    0, 1.01570004e-16, -0.829382002, 0
                    3151, -265, 1418, 1
                }
                name: string = "Info_OrderRandomThingy02"
            }
            0xd5731995 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6440.63672, -193, 7363.63672 }
                boxMax: vec3 = { 6583.36328, 92.2662048, 7506.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6512, -193, 7435, 1
                }
                name: string = "LevelProp_brush_HA_D50"
            }
            0x813cecdf = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7466.74854, -197.79007, 8328.74805 }
                boxMax: vec3 = { 7617.25146, 0.0973052979, 8479.25195 }
                0xad304db5: string = "Characters/brush_HA_B/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7542, -193, 8404, 1
                }
                name: string = "LevelProp_brush_HA_B29"
            }
            0x696a5507 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6534.78857, -194.97287, 7133.78857 }
                boxMax: vec3 = { 6665.21142, -26.9770966, 7264.21142 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6600, -193, 7199, 1
                }
                name: string = "LevelProp_brush_HA_G43"
            }
            0x5062ca7d = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 5854.33398, -111.289566, 5817.33398 }
                boxMax: vec3 = { 5957.66602, -5.95820618, 5920.66602 }
                0xad304db5: string = "Characters/ThreshLantern/Skins/Skin0"
                sceneLayer: string = "Nav Points"
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    5906, -160, 5869, 1
                }
                name: string = "__NAV_C08"
            }
            0xb92479ff = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6312.84912, -193.97934, 6828.84912 }
                boxMax: vec3 = { 6485.15088, 97.8495789, 7001.15088 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6399, -193, 6915, 1
                }
                name: string = "LevelProp_brush_HA_A46"
            }
            0x369cb7da = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5972.34766, -193, 6365.34766 }
                boxMax: vec3 = { 6081.65234, -72.1799011, 6474.65234 }
                0xad304db5: string = "Characters/brush_HA_J/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6027, -193, 6420, 1
                }
                name: string = "LevelProp_brush_HA_J21"
            }
            0x390dd95a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5455.74854, -197.79007, 6277.74854 }
                boxMax: vec3 = { 5606.25146, 0.0973052979, 6428.25146 }
                0xad304db5: string = "Characters/brush_HA_B/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5531, -193, 6353, 1
                }
                name: string = "LevelProp_brush_HA_B25"
            }
            0x444a4df6 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6351.74854, -197.79007, 6755.74854 }
                boxMax: vec3 = { 6502.25146, 0.0973052979, 6906.25146 }
                0xad304db5: string = "Characters/brush_HA_B/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6427, -193, 6831, 1
                }
                name: string = "LevelProp_brush_HA_B33"
            }
            0x9824ec4f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4054.83618, -197.79007, 5024.83594 }
                boxMax: vec3 = { 4239.16406, 0.0973052979, 5209.16406 }
                0xad304db5: string = "Characters/brush_HA_B/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.965925813, 0, 0.258819044, 0
                    0, 1, 0, 0
                    -0.258819044, 0, 0.965925813, 0
                    4147, -193, 5117, 1
                }
                name: string = "LevelProp_brush_HA_B20"
            }
            0xeae57907 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4167.84912, -193.97934, 5086.84912 }
                boxMax: vec3 = { 4340.15088, 97.8495789, 5259.15088 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4254, -193, 5173, 1
                }
                name: string = "LevelProp_brush_HA_A29"
            }
            0xbcdf7934 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5354.63672, -193, 6072.63672 }
                boxMax: vec3 = { 5497.36328, 92.2662048, 6215.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5426, -193, 6144, 1
                }
                name: string = "LevelProp_brush_HA_D34"
            }
            0xa2bb831c = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4156.34766, -193, 4974.34766 }
                boxMax: vec3 = { 4265.65234, -72.1799011, 5083.65234 }
                0xad304db5: string = "Characters/brush_HA_J/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4211, -193, 5029, 1
                }
                name: string = "LevelProp_brush_HA_J"
            }
            0x544f282e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4281.00537, -193.307343, 5172.00537 }
                boxMax: vec3 = { 4416.99463, 54.3355103, 5307.99463 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4349, -193, 5240, 1
                }
                name: string = "LevelProp_brush_HA_F28"
            }
            0x24f07e51 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5888.74854, -197.79007, 6463.74854 }
                boxMax: vec3 = { 6039.25146, 0.0973052979, 6614.25146 }
                0xad304db5: string = "Characters/brush_HA_B/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5964, -193, 6539, 1
                }
                name: string = "LevelProp_brush_HA_B28"
            }
            0x0c920872 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5528.93701, -211.859253, 6122.93701 }
                boxMax: vec3 = { 5635.06299, -75.3377075, 6229.06299 }
                0xad304db5: string = "Characters/brush_HA_I/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5582, -193, 6176, 1
                }
                name: string = "LevelProp_brush_HA_I21"
            }
            0x1f1258d0 = GdsMapObject {
                type: u8 = 9
                boxMin: vec3 = { 4751.98193, -270.068085, 3895.98193 }
                boxMax: vec3 = { 4828.01807, -188, 3972.01807 }
                0xad304db5: string = "Characters/SightWard/Skins/Skin0"
                sceneLayer: string = "Info Points"
                transform: mtx44 = {
                    0.829382002, 0, 0, 0
                    0, -0.829382002, -1.01570004e-16, 0
                    0, 1.01570004e-16, -0.829382002, 0
                    4790, -188, 3934, 1
                }
                name: string = "Info_HealthPack03"
            }
            0xe0b7662d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6468.78857, -194.97287, 7101.78857 }
                boxMax: vec3 = { 6599.21142, -26.9770966, 7232.21142 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6534, -193, 7167, 1
                }
                name: string = "LevelProp_brush_HA_G44"
            }
            0xa082632b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5177.51367, -193.858109, 6099.51367 }
                boxMax: vec3 = { 5328.48633, 61.8461914, 6250.48633 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.876213014, 0, 0, 0
                    0, 0.876213014, 0, 0
                    0, 0, 0.876213014, 0
                    5253, -193, 6175, 1
                }
                name: string = "LevelProp_brush_HA_A31"
            }
            0xc3230fa6 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4223.70361, -193.082001, 5054.70361 }
                boxMax: vec3 = { 4262.29639, -80.8568039, 5093.29639 }
                0xad304db5: string = "Characters/brush_HA_H/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4243, -193, 5074, 1
                }
                name: string = "LevelProp_brush_HA_H"
            }
            0xd642602f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7626.36523, -193, 8431.36523 }
                boxMax: vec3 = { 7745.63476, 45.3829803, 8550.63476 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.83565098, 0, 0, 0
                    0, 0.83565098, 0, 0
                    0, 0, 0.83565098, 0
                    7686, -193, 8491, 1
                }
                name: string = "LevelProp_brush_HA_D39"
            }
            0xac32ff90 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6407.63672, -193, 6907.63672 }
                boxMax: vec3 = { 6550.36328, 92.2662048, 7050.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6479, -193, 6979, 1
                }
                name: string = "LevelProp_brush_HA_D44"
            }
            0x13c03daa = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7493.52881, -193.789734, 8377.5293 }
                boxMax: vec3 = { 7632.47119, 41.5381927, 8516.4707 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.806389987, 0, 0, 0
                    0, 0.806389987, 0, 0
                    0, 0, 0.806389987, 0
                    7563, -193, 8447, 1
                }
                name: string = "LevelProp_brush_HA_A41"
            }
            0xb86d7e81 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4130.63672, -193, 5002.63672 }
                boxMax: vec3 = { 4273.36328, 92.2662048, 5145.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4202, -193, 5074, 1
                }
                name: string = "LevelProp_brush_HA_D29"
            }
            0x93775e90 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6369.97363, -204.382507, 6739.97363 }
                boxMax: vec3 = { 6434.02637, -121.984924, 6804.02637 }
                0xad304db5: string = "Characters/brush_HA_I/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.603550017, 0, 0, 0
                    0, 0.603550017, 0, 0
                    0, 0, 0.603550017, 0
                    6402, -193, 6772, 1
                }
                name: string = "LevelProp_brush_HA_I31"
            }
            0x6dcb34c8 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6299.84912, -193.97934, 6959.84912 }
                boxMax: vec3 = { 6472.15088, 97.8495789, 7132.15088 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6386, -193, 7046, 1
                }
                name: string = "LevelProp_brush_HA_A45"
            }
            0x5f1b225b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5157.93701, -211.859253, 6099.93701 }
                boxMax: vec3 = { 5264.06299, -75.3377075, 6206.06299 }
                0xad304db5: string = "Characters/brush_HA_I/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5211, -193, 6153, 1
                }
                name: string = "LevelProp_brush_HA_I23"
            }
            0x99dfb6bd = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6530.93701, -211.859253, 7043.93701 }
                boxMax: vec3 = { 6637.06299, -75.3377075, 7150.06299 }
                0xad304db5: string = "Characters/brush_HA_I/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6584, -193, 7097, 1
                }
                name: string = "LevelProp_brush_HA_I30"
            }
            0x4207afca = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4278.93701, -211.859253, 5244.93701 }
                boxMax: vec3 = { 4385.06299, -75.3377075, 5351.06299 }
                0xad304db5: string = "Characters/brush_HA_I/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4332, -193, 5298, 1
                }
                name: string = "LevelProp_brush_HA_I20"
            }
            0xad9ca93c = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4117.74854, -197.79007, 5164.74854 }
                boxMax: vec3 = { 4268.25146, 0.0973052979, 5315.25146 }
                0xad304db5: string = "Characters/brush_HA_B/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4193, -193, 5240, 1
                }
                name: string = "LevelProp_brush_HA_B21"
            }
            0xf19dda56 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 2292.12891, -113.290054, 2704.95996 }
                boxMax: vec3 = { 2395.46094, -7.95869446, 2808.29199 }
                0xad304db5: string = "Characters/ThreshLantern/Skins/Skin0"
                sceneLayer: string = "Nav Points"
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    2343.79492, -162.000488, 2756.62598, 1
                }
                name: string = "__NAV_C02"
            }
            0x669d69b9 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6311.51562, -193, 7066.51562 }
                boxMax: vec3 = { 6506.48438, 92.2662048, 7261.48438 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.866025388, 0, 0.5, 0
                    0, 1, 0, 0
                    -0.5, 0, 0.866025388, 0
                    6409, -193, 7164, 1
                }
                name: string = "LevelProp_brush_HA_D49"
            }
            0x2d09206b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7673.8208, -193, 8491.82031 }
                boxMax: vec3 = { 7818.1792, 64.7111816, 8636.17969 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.795062006, 0, 0, 0
                    0, 0.795062006, 0, 0
                    0, 0, 0.795062006, 0
                    7746, -193, 8564, 1
                }
                name: string = "LevelProp_brush_HA_C32"
            }
            0xeb1b000e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4067.63647, -193, 4967.63672 }
                boxMax: vec3 = { 4210.36328, 92.2662048, 5110.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4139, -193, 5039, 1
                }
                name: string = "LevelProp_brush_HA_D26"
            }
            0x84856fef = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6465.02441, -193, 7252.02441 }
                boxMax: vec3 = { 6610.97558, 67.5535278, 7397.97558 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.803830981, 0, 0, 0
                    0, 0.803830981, 0, 0
                    0, 0, 0.803830981, 0
                    6538, -193, 7325, 1
                }
                name: string = "LevelProp_brush_HA_C41"
            }
            0x9c28ad9d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6458.84912, -193.97934, 7157.84912 }
                boxMax: vec3 = { 6631.15088, 97.8495789, 7330.15088 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6545, -193, 7244, 1
                }
                name: string = "LevelProp_brush_HA_A50"
            }
            0x83c8975c = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7789.70361, -193.082001, 8493.70312 }
                boxMax: vec3 = { 7828.29639, -80.8568039, 8532.29688 }
                0xad304db5: string = "Characters/brush_HA_H/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7809, -193, 8513, 1
                }
                name: string = "LevelProp_brush_HA_H23"
            }
            0x9b7516eb = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6439.63672, -193, 6973.63672 }
                boxMax: vec3 = { 6582.36328, 92.2662048, 7116.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6511, -193, 7045, 1
                }
                name: string = "LevelProp_brush_HA_D47"
            }
            0xd059a02b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5344.96777, -193.784744, 6271.96777 }
                boxMax: vec3 = { 5483.03223, 40.0560303, 6410.03223 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.801294029, 0, 0, 0
                    0, 0.801294029, 0, 0
                    0, 0, 0.801294029, 0
                    5414, -193, 6341, 1
                }
                name: string = "LevelProp_brush_HA_A32"
            }
            0x13456034 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5683.93701, -211.859253, 6251.93701 }
                boxMax: vec3 = { 5790.06299, -75.3377075, 6358.06299 }
                0xad304db5: string = "Characters/brush_HA_I/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5737, -193, 6305, 1
                }
                name: string = "LevelProp_brush_HA_I24"
            }
            0xcc70d173 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7524.33447, -193, 8411.33398 }
                boxMax: vec3 = { 7661.66553, 57.0886841, 8548.66602 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.919147015, 0, 0, 0
                    0, 0.919147015, 0, 0
                    0, 0, 0.919147015, 0
                    7593, -193, 8480, 1
                }
                name: string = "LevelProp_brush_HA_E39"
            }
            0x1593682d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6266.82617, -193, 6866.82617 }
                boxMax: vec3 = { 6417.17383, 75.4032288, 7017.17383 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.828047991, 0, 0, 0
                    0, 0.828047991, 0, 0
                    0, 0, 0.828047991, 0
                    6342, -193, 6942, 1
                }
                name: string = "LevelProp_brush_HA_C38"
            }
            0x4ed35c50 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6244.78857, -194.97287, 6675.78857 }
                boxMax: vec3 = { 6375.21142, -26.9770966, 6806.21142 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6310, -193, 6741, 1
                }
                name: string = "LevelProp_brush_HA_G42"
            }
            0x78d98627 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5718.81201, -220, 6132.81201 }
                boxMax: vec3 = { 5941.18799, 104.139709, 6355.18799 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.965925813, 0, 0.258819044, 0
                    0, 1, 0, 0
                    -0.258819044, 0, 0.965925813, 0
                    5830, -220, 6244, 1
                }
                name: string = "LevelProp_brush_HA_C29"
            }
            0x5a66c12c = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4102.68262, -193, 5068.68262 }
                boxMax: vec3 = { 4261.31738, 90.1972961, 5227.31738 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.873688996, 0, 0, 0
                    0, 0.873688996, 0, 0
                    0, 0, 0.873688996, 0
                    4182, -193, 5148, 1
                }
                name: string = "LevelProp_brush_HA_C"
            }
            0x6286c917 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10367.1182, -384, 8370.11816 }
                boxMax: vec3 = { 10416.8818, -346.844543, 8419.88184 }
                0xad304db5: string = "Characters/HA_AP_Poro_Small/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.967956722, 0, -0.25111708, 0
                    0, 1, 0, 0
                    0.25111708, 0, -0.967956722, 0
                    10392, -384, 8395, 1
                }
                name: string = "LevelProp_HA_AP_Poro_Small"
            }
            0x60ec77f5 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10498.7305, -383.912292, 8355.73047 }
                boxMax: vec3 = { 10577.2695, -334.541901, 8434.26953 }
                0xad304db5: string = "Characters/HA_AP_Poro/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.848842919, 0, 0.528645098, 0
                    0, 1, 0, 0
                    -0.528645098, 0, -0.848842919, 0
                    10538, -385, 8395, 1
                }
                name: string = "LevelProp_HA_AP_Poro4"
            }
            0xef5ba73e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 3982.84912, -193.97934, 4992.84912 }
                boxMax: vec3 = { 4155.15088, 97.8495789, 5165.15088 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4069, -193, 5079, 1
                }
                name: string = "LevelProp_brush_HA_A27"
            }
            0x7149e018 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7726.78857, -194.97287, 8493.78906 }
                boxMax: vec3 = { 7857.21142, -26.9770966, 8624.21094 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7792, -193, 8559, 1
                }
                name: string = "LevelProp_brush_HA_G35"
            }
            0x989fd474 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5257.34766, -193, 6286.34766 }
                boxMax: vec3 = { 5366.65234, -72.1799011, 6395.65234 }
                0xad304db5: string = "Characters/brush_HA_J/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5312, -193, 6341, 1
                }
                name: string = "LevelProp_brush_HA_J20"
            }
            0xf5327851 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4161.78857, -194.97287, 5054.78857 }
                boxMax: vec3 = { 4292.21142, -26.9770966, 5185.21142 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4227, -193, 5120, 1
                }
                name: string = "LevelProp_brush_HA_G"
            }
            0x1bd6093e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7415.93701, -211.859253, 8369.93652 }
                boxMax: vec3 = { 7522.06299, -75.3377075, 8476.06348 }
                0xad304db5: string = "Characters/brush_HA_I/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7469, -193, 8423, 1
                }
                name: string = "LevelProp_brush_HA_I28"
            }
            0xe57435b3 = GdsMapObject {
                type: u8 = 9
                boxMin: vec3 = { 1462.98206, -347.068085, 1581.98206 }
                boxMax: vec3 = { 1539.01794, -265, 1658.01794 }
                0xad304db5: string = "Characters/SightWard/Skins/Skin0"
                sceneLayer: string = "Info Points"
                transform: mtx44 = {
                    0.829382002, 0, 0, 0
                    0, -0.829382002, -1.01570004e-16, 0
                    0, 1.01570004e-16, -0.829382002, 0
                    1501, -265, 1620, 1
                }
                name: string = "Info_OrderRandomThingy01"
            }
            0x3231dbdf = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6465.00537, -193.307343, 7205.00537 }
                boxMax: vec3 = { 6600.99463, 54.3355103, 7340.99463 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6533, -193, 7273, 1
                }
                name: string = "LevelProp_brush_HA_F48"
            }
            0xdc9b0ed0 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6620.00537, -228.307343, 7415.00537 }
                boxMax: vec3 = { 6755.99463, 19.3355103, 7550.99463 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6688, -228, 7483, 1
                }
                name: string = "LevelProp_brush_HA_F50"
            }
            0x97065132 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4087.3479, -210, 4922.34766 }
                boxMax: vec3 = { 4196.65234, -89.1799011, 5031.65234 }
                0xad304db5: string = "Characters/brush_HA_J/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4142, -210, 4977, 1
                }
                name: string = "LevelProp_brush_HA_J16"
            }
            0xaeace4f2 = GdsMapObject {
                type: u8 = 3
                boxMin: vec3 = { 9484.43848, -676.674927, 9317.42676 }
                boxMax: vec3 = { 9899.6875, 89.2898865, 9765.74512 }
                0xad304db5: string = "Characters/OrderInhibitor/Skins/Skin1"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.0174524058, 0, 0.99984771, 0
                    0, 1, 0, 0
                    -0.99984771, 0, 0.0174524058, 0
                    9690, -190, 9520, 1
                }
                name: string = "Barracks_T2_C1"
            }
            0xa210cf19 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4113.29394, -193, 5129.29394 }
                boxMax: vec3 = { 4262.70605, 79.0877991, 5278.70605 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4188, -193, 5204, 1
                }
                name: string = "LevelProp_brush_HA_E25"
            }
            0x2e3cbb53 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6536.63672, -193, 7398.63672 }
                boxMax: vec3 = { 6679.36328, 92.2662048, 7541.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6608, -193, 7470, 1
                }
                name: string = "LevelProp_brush_HA_D48"
            }
            0x4c24c64d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5401.34766, -215, 6063.34766 }
                boxMax: vec3 = { 5510.65234, -94.1799011, 6172.65234 }
                0xad304db5: string = "Characters/brush_HA_J/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5456, -215, 6118, 1
                }
                name: string = "LevelProp_brush_HA_J19"
            }
            0x6314a1dd = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6567.93701, -211.859253, 7318.93701 }
                boxMax: vec3 = { 6674.06299, -75.3377075, 7425.06299 }
                0xad304db5: string = "Characters/brush_HA_I/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6621, -193, 7372, 1
                }
                name: string = "LevelProp_brush_HA_I34"
            }
            0xa6b994d7 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 11076.1894, -779.912292, 12544.1894 }
                boxMax: vec3 = { 11143.8105, -730.541931, 12611.8105 }
                0xad304db5: string = "Characters/HA_AP_Poro/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.978165925, 0, 0.207825467, 0
                    0, 1, 0, 0
                    -0.207825467, 0, -0.978165925, 0
                    11110, -781, 12578, 1
                }
                name: string = "LevelProp_HA_AP_Poro3"
            }
            0x25d5a1dc = GdsMapObject {
                type: u8 = 3
                boxMin: vec3 = { 2896.4751, -687.260498, 2986.35596 }
                boxMax: vec3 = { 3344.7937, 78.7042923, 3401.60474 }
                0xad304db5: string = "Characters/OrderInhibitor/Skins/Skin1"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.99984771, 0, -0.0174524058, 0
                    0, 1, 0, 0
                    0.0174524058, 0, 0.99984771, 0
                    3099, -201, 3196, 1
                }
                name: string = "Barracks_T1_C1"
            }
            0xe9b68108 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5872.44238, -193, 6393.44238 }
                boxMax: vec3 = { 6013.55762, 58.9213715, 6534.55762 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.777199984, 0, 0, 0
                    0, 0.777199984, 0, 0
                    0, 0, 0.777199984, 0
                    5943, -193, 6464, 1
                }
                name: string = "LevelProp_brush_HA_C31"
            }
            0xc5129093 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7659.63672, -193, 8554.63672 }
                boxMax: vec3 = { 7802.36328, 92.2662048, 8697.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7731, -193, 8626, 1
                }
                name: string = "LevelProp_brush_HA_D41"
            }
            0x7c7d61b3 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 7150.33398, -111.289566, 7243.33398 }
                boxMax: vec3 = { 7253.66602, -5.95820618, 7346.66602 }
                0xad304db5: string = "Characters/ThreshLantern/Skins/Skin0"
                sceneLayer: string = "Nav Points"
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    7202, -160, 7295, 1
                }
                name: string = "__NAV_C011"
            }
            0x8e134a54 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7576.93701, -231.859253, 8312.93652 }
                boxMax: vec3 = { 7683.06299, -95.3377075, 8419.06348 }
                0xad304db5: string = "Characters/brush_HA_I/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7630, -213, 8366, 1
                }
                name: string = "LevelProp_brush_HA_I27"
            }
            0x3a88be85 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7619.74854, -197.79007, 8456.74805 }
                boxMax: vec3 = { 7770.25146, 0.0973052979, 8607.25195 }
                0xad304db5: string = "Characters/brush_HA_B/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7695, -193, 8532, 1
                }
                name: string = "LevelProp_brush_HA_B30"
            }
            0xf37ea7dc = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4093.00562, -193.307343, 4997.00537 }
                boxMax: vec3 = { 4228.99463, 54.3355103, 5132.99463 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4161, -193, 5065, 1
                }
                name: string = "LevelProp_brush_HA_F26"
            }
            0x34fd0c0d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4039.84912, -193.97934, 5086.84912 }
                boxMax: vec3 = { 4212.15088, 97.8495789, 5259.15088 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4126, -193, 5173, 1
                }
                name: string = "LevelProp_brush_HA_A26"
            }
            0x766c9873 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7842.00537, -193.307343, 8611.00586 }
                boxMax: vec3 = { 7977.99463, 54.3355103, 8746.99414 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7910, -193, 8679, 1
                }
                name: string = "LevelProp_brush_HA_F41"
            }
            0xdc5540e3 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7805.74854, -197.79007, 8637.74805 }
                boxMax: vec3 = { 7956.25146, 0.0973052979, 8788.25195 }
                0xad304db5: string = "Characters/brush_HA_B/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7881, -193, 8713, 1
                }
                name: string = "LevelProp_brush_HA_B32"
            }
            0x7c60b1f4 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5252.44189, -193.76799, 6159.44189 }
                boxMax: vec3 = { 5387.5581, 35.0792999, 6294.5581 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.784183025, 0, 0, 0
                    0, 0.784183025, 0, 0
                    0, 0, 0.784183025, 0
                    5320, -193, 6227, 1
                }
                name: string = "LevelProp_brush_HA_A34"
            }
            0xb07b8db8 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 4141.33398, -103.289566, 4503.33398 }
                boxMax: vec3 = { 4244.66602, 2.04179382, 4606.66602 }
                0xad304db5: string = "Characters/ThreshLantern/Skins/Skin0"
                sceneLayer: string = "Nav Points"
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    4193, -152, 4555, 1
                }
                name: string = "__NAV_C05"
            }
            0x8a63cf0b = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 2851.33398, -106.289566, 3359.33398 }
                boxMax: vec3 = { 2954.66602, -0.958206177, 3462.66602 }
                0xad304db5: string = "Characters/ThreshLantern/Skins/Skin0"
                sceneLayer: string = "Nav Points"
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    2903, -155, 3411, 1
                }
                name: string = "__NAV_C03"
            }
            0x40336693 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6403.84912, -193.97934, 7232.84912 }
                boxMax: vec3 = { 6576.15088, 97.8495789, 7405.15088 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6490, -193, 7319, 1
                }
                name: string = "LevelProp_brush_HA_A49"
            }
            0x9f60e82d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5357.63672, -193, 6240.63672 }
                boxMax: vec3 = { 5500.36328, 92.2662048, 6383.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5429, -193, 6312, 1
                }
                name: string = "LevelProp_brush_HA_D33"
            }
            0x1284a51f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5931.78857, -194.97287, 6375.78857 }
                boxMax: vec3 = { 6062.21142, -26.9770966, 6506.21142 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5997, -193, 6441, 1
                }
                name: string = "LevelProp_brush_HA_G34"
            }
            0xd01b2337 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6224.44922, -193, 6724.44922 }
                boxMax: vec3 = { 6353.55078, 37.4740295, 6853.55078 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.711032987, 0, 0, 0
                    0, 0.711032987, 0, 0
                    0, 0, 0.711032987, 0
                    6289, -193, 6789, 1
                }
                name: string = "LevelProp_brush_HA_C39"
            }
            0xa4be5ecb = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5886.63672, -225, 6282.63672 }
                boxMax: vec3 = { 6029.36328, 60.2662048, 6425.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5958, -225, 6354, 1
                }
                name: string = "LevelProp_brush_HA_D35"
            }
            0x8859b6d1 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7848.94678, -193.271439, 8560.94726 }
                boxMax: vec3 = { 7969.05322, 25.4482117, 8681.05273 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.88320601, 0, 0, 0
                    0, 0.88320601, 0, 0
                    0, 0, 0.88320601, 0
                    7909, -193, 8621, 1
                }
                name: string = "LevelProp_brush_HA_F40"
            }
            0x2a7f2fe7 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5558.84912, -193.97934, 6156.84912 }
                boxMax: vec3 = { 5731.15088, 97.8495789, 6329.15088 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5645, -193, 6243, 1
                }
                name: string = "LevelProp_brush_HA_A35"
            }
            0x6223a427 = GdsMapObject {
                boxMin: vec3 = { 10505.4414, -182.639496, 10360.4414 }
                boxMax: vec3 = { 10782.5586, -18.3764648, 10637.5586 }
                0xad304db5: string = "Characters/SRU_OrderMinionSuper/Skins/Skin0"
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    10644, -182, 10499, 1
                }
                name: string = "____P_Chaos_Spawn_Barracks__C01"
            }
            0xdcaa9527 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6201.70361, -199.082001, 6750.70361 }
                boxMax: vec3 = { 6240.29639, -86.8568039, 6789.29639 }
                0xad304db5: string = "Characters/brush_HA_H/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6221, -199, 6770, 1
                }
                name: string = "LevelProp_brush_HA_H28"
            }
            0xad9a23bd = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4098.63672, -193, 5141.63672 }
                boxMax: vec3 = { 4241.36328, 92.2662048, 5284.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4170, -193, 5213, 1
                }
                name: string = "LevelProp_brush_HA_D28"
            }
            0xc3f2d5e3 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6422.74854, -197.79007, 7311.74854 }
                boxMax: vec3 = { 6573.25146, 0.0973052979, 7462.25146 }
                0xad304db5: string = "Characters/brush_HA_B/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6498, -193, 7387, 1
                }
                name: string = "LevelProp_brush_HA_B37"
            }
            0x3c541f86 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5418.00537, -193.307343, 6275.00537 }
                boxMax: vec3 = { 5553.99463, 54.3355103, 6410.99463 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5486, -193, 6343, 1
                }
                name: string = "LevelProp_brush_HA_F34"
            }
            0x97792d68 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7859.7251, -193, 8585.72461 }
                boxMax: vec3 = { 8004.2749, 65.0527954, 8730.27539 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.796115994, 0, 0, 0
                    0, 0.796115994, 0, 0
                    0, 0, 0.796115994, 0
                    7932, -193, 8658, 1
                }
                name: string = "LevelProp_brush_HA_C35"
            }
            0xc812ab93 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5667.00537, -193.307343, 6159.00537 }
                boxMax: vec3 = { 5802.99463, 54.3355103, 6294.99463 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5735, -193, 6227, 1
                }
                name: string = "LevelProp_brush_HA_F32"
            }
            0x2b3aca4a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6372.00537, -193.307343, 6873.00537 }
                boxMax: vec3 = { 6507.99463, 54.3355103, 7008.99463 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6440, -193, 6941, 1
                }
                name: string = "LevelProp_brush_HA_F44"
            }
            0x74f9ee15 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6405.29394, -193, 6826.29394 }
                boxMax: vec3 = { 6554.70605, 79.0877991, 6975.70605 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6480, -193, 6901, 1
                }
                name: string = "LevelProp_brush_HA_E40"
            }
            0xe46cc0cd = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7579.00684, -185, 8320.00684 }
                boxMax: vec3 = { 7696.99316, 50.8178864, 8437.99316 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.826659024, 0, 0, 0
                    0, 0.826659024, 0, 0
                    0, 0, 0.826659024, 0
                    7638, -185, 8379, 1
                }
                name: string = "LevelProp_brush_HA_D40"
            }
            0x5b70467d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5939.00537, -193.307343, 6307.00537 }
                boxMax: vec3 = { 6074.99463, 54.3355103, 6442.99463 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6007, -193, 6375, 1
                }
                name: string = "LevelProp_brush_HA_F37"
            }
            0xbf08cadb = GdsMapObject {
                boxMin: vec3 = { 2009.44153, -182.639496, 2082.44141 }
                boxMax: vec3 = { 2286.55859, -18.3764648, 2359.55859 }
                0xad304db5: string = "Characters/SRU_OrderMinionSuper/Skins/Skin0"
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    2148, -182, 2221, 1
                }
                name: string = "____P_Order_Spawn_Barracks__C01"
            }
            0x719ac069 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7657.89941, -193, 8408.89941 }
                boxMax: vec3 = { 7784.10058, 36.8200531, 8535.10058 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.844654024, 0, 0, 0
                    0, 0.844654024, 0, 0
                    0, 0, 0.844654024, 0
                    7721, -193, 8472, 1
                }
                name: string = "LevelProp_brush_HA_E35"
            }
            0xd28d1677 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6576.70361, -220.082001, 7135.70361 }
                boxMax: vec3 = { 6615.29639, -107.856804, 7174.29639 }
                0xad304db5: string = "Characters/brush_HA_H/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6596, -220, 7155, 1
                }
                name: string = "LevelProp_brush_HA_H27"
            }
            0x32067af5 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5754.70361, -193.082001, 6384.70361 }
                boxMax: vec3 = { 5793.29639, -80.8568039, 6423.29639 }
                0xad304db5: string = "Characters/brush_HA_H/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5774, -193, 6404, 1
                }
                name: string = "LevelProp_brush_HA_H22"
            }
            0xe7a9c48f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5292.01123, -232.859253, 6042.01123 }
                boxMax: vec3 = { 5421.98877, -96.3377075, 6171.98877 }
                0xad304db5: string = "Characters/brush_HA_I/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.965925813, 0, -0.258819044, 0
                    0, 1, 0, 0
                    0.258819044, 0, 0.965925813, 0
                    5357, -214, 6107, 1
                }
                name: string = "LevelProp_brush_HA_I22"
            }
            0xaf7218d7 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 9408.33398, -125.289566, 9669.33398 }
                boxMax: vec3 = { 9511.66602, -19.9582062, 9772.66602 }
                0xad304db5: string = "Characters/ThreshLantern/Skins/Skin0"
                sceneLayer: string = "Nav Points"
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    9460, -174, 9721, 1
                }
                name: string = "__NAV_C015"
            }
            0x59399e86 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5383.00537, -193.307343, 6202.00537 }
                boxMax: vec3 = { 5518.99463, 54.3355103, 6337.99463 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5451, -193, 6270, 1
                }
                name: string = "LevelProp_brush_HA_F31"
            }
            0x2b5fe3c3 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6400.81201, -204, 6822.81201 }
                boxMax: vec3 = { 6623.18799, 120.139709, 7045.18799 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.965925813, 0, 0.258819044, 0
                    0, 1, 0, 0
                    -0.258819044, 0, 0.965925813, 0
                    6512, -204, 6934, 1
                }
                name: string = "LevelProp_brush_HA_C37"
            }
            0xc837f1e9 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6436.74854, -197.79007, 7419.74854 }
                boxMax: vec3 = { 6587.25146, 0.0973052979, 7570.25146 }
                0xad304db5: string = "Characters/brush_HA_B/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6512, -193, 7495, 1
                }
                name: string = "LevelProp_brush_HA_B38"
            }
            0x1322ea1f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7555.70361, -209.082001, 8257.70312 }
                boxMax: vec3 = { 7594.29639, -96.8568039, 8296.29688 }
                0xad304db5: string = "Characters/brush_HA_H/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7575, -209, 8277, 1
                }
                name: string = "LevelProp_brush_HA_H25"
            }
            0x33bedd3e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4247.93701, -211.859253, 5057.93701 }
                boxMax: vec3 = { 4354.06299, -75.3377075, 5164.06299 }
                0xad304db5: string = "Characters/brush_HA_I/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4301, -193, 5111, 1
                }
                name: string = "LevelProp_brush_HA_I"
            }
            0xa53f9a3e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4292.74854, -197.79007, 5199.74854 }
                boxMax: vec3 = { 4443.25146, 0.0973052979, 5350.25146 }
                0xad304db5: string = "Characters/brush_HA_B/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4368, -193, 5275, 1
                }
                name: string = "LevelProp_brush_HA_B22"
            }
            0xc770d7a0 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6512.78857, -194.97287, 7416.78857 }
                boxMax: vec3 = { 6643.21142, -26.9770966, 7547.21142 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6578, -193, 7482, 1
                }
                name: string = "LevelProp_brush_HA_G46"
            }
            0x8399e4e3 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4359.70361, -193.082001, 5207.70361 }
                boxMax: vec3 = { 4398.29639, -80.8568039, 5246.29639 }
                0xad304db5: string = "Characters/brush_HA_H/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4379, -193, 5227, 1
                }
                name: string = "LevelProp_brush_HA_H18"
            }
            0x4e2de4fb = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7431.29443, -193.746933, 8363.29492 }
                boxMax: vec3 = { 7562.70557, 28.824585, 8494.70508 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.762678027, 0, 0, 0
                    0, 0.762678027, 0, 0
                    0, 0, 0.762678027, 0
                    7497, -193, 8429, 1
                }
                name: string = "LevelProp_brush_HA_A38"
            }
            0x91b2a1a8 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7662.78857, -194.97287, 8386.78906 }
                boxMax: vec3 = { 7793.21142, -26.9770966, 8517.21094 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7728, -193, 8452, 1
                }
                name: string = "LevelProp_brush_HA_G36"
            }
            0xdb548478 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5166.70361, -199.082001, 6153.70361 }
                boxMax: vec3 = { 5205.29639, -86.8568039, 6192.29639 }
                0xad304db5: string = "Characters/brush_HA_H/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5186, -199, 6173, 1
                }
                name: string = "LevelProp_brush_HA_H20"
            }
            0x9d13ec3f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6348.66992, -201.048157, 6685.66992 }
                boxMax: vec3 = { 6371.33008, -135.155014, 6708.33008 }
                0xad304db5: string = "Characters/brush_HA_H/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.587150991, 0, 0, 0
                    0, 0.587150991, 0, 0
                    0, 0, 0.587150991, 0
                    6360, -201, 6697, 1
                }
                name: string = "LevelProp_brush_HA_H29"
            }
            0xa236f876 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7524.67773, -192, 8268.67773 }
                boxMax: vec3 = { 7595.32226, -113.91288, 8339.32226 }
                0xad304db5: string = "Characters/brush_HA_J/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.646309018, 0, 0, 0
                    0, 0.646309018, 0, 0
                    0, 0, 0.646309018, 0
                    7560, -192, 8304, 1
                }
                name: string = "LevelProp_brush_HA_J32"
            }
            0x3f6a1d8c = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6461.29394, -193, 7315.29394 }
                boxMax: vec3 = { 6610.70605, 79.0877991, 7464.70605 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6536, -193, 7390, 1
                }
                name: string = "LevelProp_brush_HA_E42"
            }
            0x20bbdd1a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7811.78857, -194.97287, 8518.78906 }
                boxMax: vec3 = { 7942.21142, -26.9770966, 8649.21094 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7877, -193, 8584, 1
                }
                name: string = "LevelProp_brush_HA_G38"
            }
            0x9c26d4b1 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6252.84912, -193.97934, 6786.84912 }
                boxMax: vec3 = { 6425.15088, 97.8495789, 6959.15088 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6339, -193, 6873, 1
                }
                name: string = "LevelProp_brush_HA_A47"
            }
            0x8952b945 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 7543.33398, -125.289566, 7806.33398 }
                boxMax: vec3 = { 7646.66602, -19.9582062, 7909.66602 }
                0xad304db5: string = "Characters/ThreshLantern/Skins/Skin0"
                sceneLayer: string = "Nav Points"
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    7595, -174, 7858, 1
                }
                name: string = "__NAV_C012"
            }
            0xd4d64598 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 3948.70361, -193.082001, 4885.70361 }
                boxMax: vec3 = { 3987.29639, -80.8568039, 4924.29639 }
                0xad304db5: string = "Characters/brush_HA_H/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3968, -193, 4905, 1
                }
                name: string = "LevelProp_brush_HA_H16"
            }
            0x07593bd0 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6522.34766, -193, 7016.34766 }
                boxMax: vec3 = { 6631.65234, -72.1799011, 7125.65234 }
                0xad304db5: string = "Characters/brush_HA_J/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6577, -193, 7071, 1
                }
                name: string = "LevelProp_brush_HA_J26"
            }
            0xd2aa7751 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5531.29394, -210, 6234.29394 }
                boxMax: vec3 = { 5680.70605, 62.0877991, 6383.70605 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5606, -210, 6309, 1
                }
                name: string = "LevelProp_brush_HA_E30"
            }
            0x3c7dc17f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6360.63672, -193, 6954.63672 }
                boxMax: vec3 = { 6503.36328, 92.2662048, 7097.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6432, -193, 7026, 1
                }
                name: string = "LevelProp_brush_HA_D46"
            }
            0x6dd09fde = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5212.74854, -197.79007, 6117.74854 }
                boxMax: vec3 = { 5363.25146, 0.0973052979, 6268.25146 }
                0xad304db5: string = "Characters/brush_HA_B/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5288, -193, 6193, 1
                }
                name: string = "LevelProp_brush_HA_B23"
            }
            0xe06ee898 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5296.48828, -193.812927, 6220.48828 }
                boxMax: vec3 = { 5439.51172, 48.4272461, 6363.51172 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.830075979, 0, 0, 0
                    0, 0.830075979, 0, 0
                    0, 0, 0.830075979, 0
                    5368, -193, 6292, 1
                }
                name: string = "LevelProp_brush_HA_A33"
            }
            0xd547298d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5713.00537, -193.307343, 6261.00537 }
                boxMax: vec3 = { 5848.99463, 54.3355103, 6396.99463 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5781, -193, 6329, 1
                }
                name: string = "LevelProp_brush_HA_F33"
            }
            0xe33b0093 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4294.00537, -193.307343, 5109.00537 }
                boxMax: vec3 = { 4429.99463, 54.3355103, 5244.99463 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4362, -193, 5177, 1
                }
                name: string = "LevelProp_brush_HA_F27"
            }
            0x49dbf532 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7655.34766, -213, 8344.34766 }
                boxMax: vec3 = { 7764.65234, -92.1799011, 8453.65234 }
                0xad304db5: string = "Characters/brush_HA_J/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7710, -213, 8399, 1
                }
                name: string = "LevelProp_brush_HA_J24"
            }
            0x77583a29 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7761.29394, -193, 8483.29394 }
                boxMax: vec3 = { 7910.70605, 79.0877991, 8632.70605 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7836, -193, 8558, 1
                }
                name: string = "LevelProp_brush_HA_E36"
            }
            0x2a4fd5b5 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6211.38428, -193.791382, 6767.38428 }
                boxMax: vec3 = { 6350.61572, 42.0265198, 6906.61572 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.808068991, 0, 0, 0
                    0, 0.808068991, 0, 0
                    0, 0, 0.808068991, 0
                    6281, -193, 6837, 1
                }
                name: string = "LevelProp_brush_HA_A44"
            }
            0x55ffa263 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6407.70361, -193.082001, 7125.70361 }
                boxMax: vec3 = { 6446.29639, -80.8568039, 7164.29639 }
                0xad304db5: string = "Characters/brush_HA_H/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6427, -193, 7145, 1
                }
                name: string = "LevelProp_brush_HA_H30"
            }
            0xefdc5207 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7711.29394, -193, 8569.29394 }
                boxMax: vec3 = { 7860.70605, 79.0877991, 8718.70605 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7786, -193, 8644, 1
                }
                name: string = "LevelProp_brush_HA_E38"
            }
            0x08dda76f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6501.34766, -193, 6967.34766 }
                boxMax: vec3 = { 6610.65234, -72.1799011, 7076.65234 }
                0xad304db5: string = "Characters/brush_HA_J/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6556, -193, 7022, 1
                }
                name: string = "LevelProp_brush_HA_J27"
            }
            0xeae48038 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5493.34766, -215, 6095.34766 }
                boxMax: vec3 = { 5602.65234, -94.1799011, 6204.65234 }
                0xad304db5: string = "Characters/brush_HA_J/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5548, -215, 6150, 1
                }
                name: string = "LevelProp_brush_HA_J18"
            }
            0x7cf34586 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5346.70361, -216.082001, 6083.70361 }
                boxMax: vec3 = { 5385.29639, -103.856804, 6122.29639 }
                0xad304db5: string = "Characters/brush_HA_H/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5366, -216, 6103, 1
                }
                name: string = "LevelProp_brush_HA_H21"
            }
            0xd3475837 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 3926.74854, -197.79007, 4894.74854 }
                boxMax: vec3 = { 4077.25146, 0.0973052979, 5045.25146 }
                0xad304db5: string = "Characters/brush_HA_B/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4002, -193, 4970, 1
                }
                name: string = "LevelProp_brush_HA_B"
            }
            0x03fad0fd = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7528.28613, -211, 8267.28613 }
                boxMax: vec3 = { 7659.71387, 23.6262512, 8398.71387 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.723842978, 0, 0, 0
                    0, 0.723842978, 0, 0
                    0, 0, 0.723842978, 0
                    7594, -211, 8333, 1
                }
                name: string = "LevelProp_brush_HA_C34"
            }
            0xa6dd7c47 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6307.00537, -193.307343, 6656.00537 }
                boxMax: vec3 = { 6442.99463, 54.3355103, 6791.99463 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6375, -193, 6724, 1
                }
                name: string = "LevelProp_brush_HA_F43"
            }
            0xd6e5b624 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 3971.29394, -193, 4991.29394 }
                boxMax: vec3 = { 4120.70605, 79.0877991, 5140.70605 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4046, -193, 5066, 1
                }
                name: string = "LevelProp_brush_HA_E27"
            }
            0x1a82acd4 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5822.63672, -193, 6427.63672 }
                boxMax: vec3 = { 5965.36328, 92.2662048, 6570.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5894, -193, 6499, 1
                }
                name: string = "LevelProp_brush_HA_D37"
            }
            0x048a5250 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6239.82812, -193, 6843.82812 }
                boxMax: vec3 = { 6358.17188, 22.5106812, 6962.17188 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.792062998, 0, 0, 0
                    0, 0.792062998, 0, 0
                    0, 0, 0.792062998, 0
                    6299, -193, 6903, 1
                }
                name: string = "LevelProp_brush_HA_E44"
            }
            0xa517d0bf = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4185.59131, -193, 5177.59131 }
                boxMax: vec3 = { 4336.40869, 76.2408142, 5328.40869 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.830631971, 0, 0, 0
                    0, 0.830631971, 0, 0
                    0, 0, 0.830631971, 0
                    4261, -193, 5253, 1
                }
                name: string = "LevelProp_brush_HA_C25"
            }
            0x128a336e = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 8081.33398, -125.289566, 8320.33398 }
                boxMax: vec3 = { 8184.66602, -19.9582062, 8423.66602 }
                0xad304db5: string = "Characters/ThreshLantern/Skins/Skin0"
                sceneLayer: string = "Nav Points"
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    8133, -174, 8372, 1
                }
                name: string = "__NAV_C013"
            }
            0xf743305e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4018.00562, -192.307343, 4898.00537 }
                boxMax: vec3 = { 4153.99463, 55.3355103, 5033.99463 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4086, -192, 4966, 1
                }
                name: string = "LevelProp_brush_HA_F"
            }
            0x38ce5498 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5389.29394, -193, 6113.29394 }
                boxMax: vec3 = { 5538.70605, 79.0877991, 6262.70605 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5464, -193, 6188, 1
                }
                name: string = "LevelProp_brush_HA_E28"
            }
            0x9dae4e81 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5619.47461, -193.801727, 6292.47461 }
                boxMax: vec3 = { 5760.52539, 45.0976105, 6433.52539 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.818628013, 0, 0, 0
                    0, 0.818628013, 0, 0
                    0, 0, 0.818628013, 0
                    5690, -193, 6363, 1
                }
                name: string = "LevelProp_brush_HA_A36"
            }
            0x41873951 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5567.09814, -215.29628, 6062.09814 }
                boxMax: vec3 = { 5718.90186, -19.7602997, 6213.90186 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1.16393399, 0, 0, 0
                    0, 1.16393399, 0, 0
                    0, 0, 1.16393399, 0
                    5643, -213, 6138, 1
                }
                name: string = "LevelProp_brush_HA_G31"
            }
            0x547ddfca = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 3940.63647, -193, 4852.63672 }
                boxMax: vec3 = { 4083.36353, 92.2662048, 4995.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4012, -193, 4924, 1
                }
                name: string = "LevelProp_brush_HA_D27"
            }
            0x94d69ce0 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7786.41211, -193.722855, 8661.41211 }
                boxMax: vec3 = { 7913.58789, 21.6757812, 8788.58789 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.738098979, 0, 0, 0
                    0, 0.738098979, 0, 0
                    0, 0, 0.738098979, 0
                    7850, -193, 8725, 1
                }
                name: string = "LevelProp_brush_HA_A43"
            }
            0x46d5c254 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6470.29394, -193, 7430.29394 }
                boxMax: vec3 = { 6619.70605, 79.0877991, 7579.70605 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6545, -193, 7505, 1
                }
                name: string = "LevelProp_brush_HA_E46"
            }
            0xf27e0e1e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6586.29394, -193, 7283.29394 }
                boxMax: vec3 = { 6735.70605, 79.0877991, 7432.70605 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6661, -193, 7358, 1
                }
                name: string = "LevelProp_brush_HA_E41"
            }
            0x01fc9a4c = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 4712.33398, -105.289566, 5014.33398 }
                boxMax: vec3 = { 4815.66602, 0.0417938232, 5117.66602 }
                0xad304db5: string = "Characters/ThreshLantern/Skins/Skin0"
                sceneLayer: string = "Nav Points"
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    4764, -154, 5066, 1
                }
                name: string = "__NAV_C06"
            }
            0x49a275a5 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 2119.35303, -114.912292, 4323.35303 }
                boxMax: vec3 = { 2182.64697, -65.5419083, 4386.64697 }
                0xad304db5: string = "Characters/HA_AP_Poro/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.993137658, 0, 0.116951041, 0
                    0, 1, 0, 0
                    -0.116951041, 0, -0.993137658, 0
                    2151, -116, 4355, 1
                }
                name: string = "LevelProp_HA_AP_Poro1"
            }
            0xb835c643 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7705.79785, -193, 8451.79785 }
                boxMax: vec3 = { 7828.20215, 51.6471405, 8574.20215 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.857609987, 0, 0, 0
                    0, 0.857609987, 0, 0
                    0, 0, 0.857609987, 0
                    7767, -193, 8513, 1
                }
                name: string = "LevelProp_brush_HA_D42"
            }
            0x6befe3de = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 3993.42432, -193, 4945.42432 }
                boxMax: vec3 = { 4150.57568, 87.5490723, 5102.57568 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.865518987, 0, 0, 0
                    0, 0.865518987, 0, 0
                    0, 0, 0.865518987, 0
                    4072, -193, 5024, 1
                }
                name: string = "LevelProp_brush_HA_C22"
            }
            0x525df8ce = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5829.63672, -193, 6308.63672 }
                boxMax: vec3 = { 5972.36328, 92.2662048, 6451.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5901, -193, 6380, 1
                }
                name: string = "LevelProp_brush_HA_D36"
            }
            0xfd482cfa = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5233.23291, -214, 6063.23291 }
                boxMax: vec3 = { 5368.76709, 27.9566803, 6198.76709 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.746457994, 0, 0, 0
                    0, 0.746457994, 0, 0
                    0, 0, 0.746457994, 0
                    5301, -214, 6131, 1
                }
                name: string = "LevelProp_brush_HA_C28"
            }
            0x2466a0c8 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4184.45654, -193, 5032.45654 }
                boxMax: vec3 = { 4357.54346, 79.0877991, 5205.54346 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.98480773, 0, 0.173648164, 0
                    0, 1, 0, 0
                    -0.173648164, 0, 0.98480773, 0
                    4271, -193, 5119, 1
                }
                name: string = "LevelProp_brush_HA_E24"
            }
            0x561e58f6 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6337.00537, -193.307343, 7020.00537 }
                boxMax: vec3 = { 6472.99463, 54.3355103, 7155.99463 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6405, -193, 7088, 1
                }
                name: string = "LevelProp_brush_HA_F47"
            }
            0xb9a18657 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 10135.334, -125.289566, 10219.334 }
                boxMax: vec3 = { 10238.666, -19.9582062, 10322.666 }
                0xad304db5: string = "Characters/ThreshLantern/Skins/Skin0"
                sceneLayer: string = "Nav Points"
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    10187, -174, 10271, 1
                }
                name: string = "__NAV_C016"
            }
            0x67bb4905 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6394.00537, -193.307343, 7151.00537 }
                boxMax: vec3 = { 6529.99463, 54.3355103, 7286.99463 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6462, -193, 7219, 1
                }
                name: string = "LevelProp_brush_HA_F46"
            }
            0x9f82791e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5663.78857, -194.97287, 6308.78857 }
                boxMax: vec3 = { 5794.21142, -26.9770966, 6439.21142 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5729, -193, 6374, 1
                }
                name: string = "LevelProp_brush_HA_G32"
            }
            0xea97f127 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 12802.7158, -900.912292, 9659.71582 }
                boxMax: vec3 = { 12883.2842, -851.541931, 9740.28418 }
                0xad304db5: string = "Characters/HA_AP_Poro/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.677968383, 0, 0.735091031, 0
                    0, 1, 0, 0
                    -0.735091031, 0, -0.677968383, 0
                    12843, -902, 9700, 1
                }
                name: string = "LevelProp_HA_AP_Poro5"
            }
            0x2f8738b6 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 6382.33398, -111.289566, 6162.33398 }
                boxMax: vec3 = { 6485.66602, -5.95820618, 6265.66602 }
                0xad304db5: string = "Characters/ThreshLantern/Skins/Skin0"
                sceneLayer: string = "Nav Points"
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    6434, -160, 6214, 1
                }
                name: string = "__NAV_C09"
            }
            0x78a2a295 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5664.70361, -216.082001, 6222.70361 }
                boxMax: vec3 = { 5703.29639, -103.856804, 6261.29639 }
                0xad304db5: string = "Characters/brush_HA_H/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5684, -216, 6242, 1
                }
                name: string = "LevelProp_brush_HA_H19"
            }
            0xa51a0485 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7722.34766, -217, 8413.34766 }
                boxMax: vec3 = { 7831.65234, -96.1799011, 8522.65234 }
                0xad304db5: string = "Characters/brush_HA_J/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7777, -217, 8468, 1
                }
                name: string = "LevelProp_brush_HA_J23"
            }
            0x3261622e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5186.29394, -193, 6205.29394 }
                boxMax: vec3 = { 5335.70605, 79.0877991, 6354.70605 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5261, -193, 6280, 1
                }
                name: string = "LevelProp_brush_HA_E32"
            }
            0x3d504171 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4079.78882, -194.97287, 4919.78857 }
                boxMax: vec3 = { 4210.21142, -26.9770966, 5050.21142 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4145, -193, 4985, 1
                }
                name: string = "LevelProp_brush_HA_G24"
            }
            0xcf76d14b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5801.93701, -229.859253, 6210.93701 }
                boxMax: vec3 = { 5908.06299, -93.3377075, 6317.06299 }
                0xad304db5: string = "Characters/brush_HA_I/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5855, -211, 6264, 1
                }
                name: string = "LevelProp_brush_HA_I25"
            }
            0x11e37de5 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5764.74854, -203.79007, 6359.74854 }
                boxMax: vec3 = { 5915.25146, -5.9026947, 6510.25146 }
                0xad304db5: string = "Characters/brush_HA_B/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5840, -199, 6435, 1
                }
                name: string = "LevelProp_brush_HA_B27"
            }
            0x26d1f07a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7539.78857, -186.97287, 8245.78906 }
                boxMax: vec3 = { 7670.21142, -18.9770966, 8376.21094 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7605, -185, 8311, 1
                }
                name: string = "LevelProp_brush_HA_G37"
            }
            0x84fb9836 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4049.29394, -193, 4937.29394 }
                boxMax: vec3 = { 4198.70605, 79.0877991, 5086.70605 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4124, -193, 5012, 1
                }
                name: string = "LevelProp_brush_HA_E"
            }
            0x7f7a4888 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7744.92676, -193.864792, 8544.92676 }
                boxMax: vec3 = { 7897.07324, 63.8277283, 8697.07324 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.883026004, 0, 0, 0
                    0, 0.883026004, 0, 0
                    0, 0, 0.883026004, 0
                    7821, -193, 8621, 1
                }
                name: string = "LevelProp_brush_HA_A42"
            }
            0xa1adc0b6 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 5257.33398, -111.289566, 5430.33398 }
                boxMax: vec3 = { 5360.66602, -5.95820618, 5533.66602 }
                0xad304db5: string = "Characters/ThreshLantern/Skins/Skin0"
                sceneLayer: string = "Nav Points"
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    5309, -160, 5482, 1
                }
                name: string = "__NAV_C07"
            }
            0x75a47af9 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5355.63672, -193, 6149.63672 }
                boxMax: vec3 = { 5498.36328, 92.2662048, 6292.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5427, -193, 6221, 1
                }
                name: string = "LevelProp_brush_HA_D31"
            }
            0x418bbe26 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5840.00537, -207.307343, 6352.00537 }
                boxMax: vec3 = { 5975.99463, 40.3355103, 6487.99463 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5908, -207, 6420, 1
                }
                name: string = "LevelProp_brush_HA_F36"
            }
            0x391bb407 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6377.78857, -194.97287, 6798.78857 }
                boxMax: vec3 = { 6508.21142, -26.9770966, 6929.21142 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6443, -193, 6864, 1
                }
                name: string = "LevelProp_brush_HA_G41"
            }
            0xf7a6bebd = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7658.00537, -193.307343, 8436.00586 }
                boxMax: vec3 = { 7793.99463, 54.3355103, 8571.99414 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7726, -193, 8504, 1
                }
                name: string = "LevelProp_brush_HA_F39"
            }
            0xc8c500ea = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6307.34766, -193, 6970.34766 }
                boxMax: vec3 = { 6416.65234, -72.1799011, 7079.65234 }
                0xad304db5: string = "Characters/brush_HA_J/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6362, -193, 7025, 1
                }
                name: string = "LevelProp_brush_HA_J28"
            }
            0xe2fb970b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7843.93701, -211.859253, 8683.93652 }
                boxMax: vec3 = { 7950.06299, -75.3377075, 8790.06348 }
                0xad304db5: string = "Characters/brush_HA_I/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7897, -193, 8737, 1
                }
                name: string = "LevelProp_brush_HA_I29"
            }
            0x8db09756 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 3902.77417, -204, 4872.77441 }
                boxMax: vec3 = { 3969.22583, -130.547546, 4939.22558 }
                0xad304db5: string = "Characters/brush_HA_J/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.607949018, 0, 0, 0
                    0, 0.607949018, 0, 0
                    0, 0, 0.607949018, 0
                    3936, -204, 4906, 1
                }
                name: string = "LevelProp_brush_HA_J31"
            }
            0xf5ee0254 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 3882.93677, -211.859253, 4892.93701 }
                boxMax: vec3 = { 3989.06323, -75.3377075, 4999.06299 }
                0xad304db5: string = "Characters/brush_HA_I/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3936, -193, 4946, 1
                }
                name: string = "LevelProp_brush_HA_I19"
            }
            0x53ae468a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5775.00537, -193.307343, 6264.00537 }
                boxMax: vec3 = { 5910.99463, 54.3355103, 6399.99463 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5843, -193, 6332, 1
                }
                name: string = "LevelProp_brush_HA_F35"
            }
            0x06caac7d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4239.63672, -193, 5124.63672 }
                boxMax: vec3 = { 4382.36328, 92.2662048, 5267.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4311, -193, 5196, 1
                }
                name: string = "LevelProp_brush_HA_D"
            }
            0x75ef9ea4 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7751.00537, -193.307343, 8459.00586 }
                boxMax: vec3 = { 7886.99463, 54.3355103, 8594.99414 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7819, -193, 8527, 1
                }
                name: string = "LevelProp_brush_HA_F42"
            }
            0x2e452e7f = GdsMapObject {
                type: u8 = 9
                boxMin: vec3 = { 8854.98242, -269.068085, 7850.98193 }
                boxMax: vec3 = { 8931.01758, -187, 7927.01807 }
                0xad304db5: string = "Characters/SightWard/Skins/Skin0"
                sceneLayer: string = "Info Points"
                transform: mtx44 = {
                    0.829382002, 0, 0, 0
                    0, -0.829382002, -1.01570004e-16, 0
                    0, 1.01570004e-16, -0.829382002, 0
                    8893, -187, 7889, 1
                }
                name: string = "Info_HealthPack02"
            }
            0x9db0ea38 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6576.34766, -193, 7379.34766 }
                boxMax: vec3 = { 6685.65234, -72.1799011, 7488.65234 }
                0xad304db5: string = "Characters/brush_HA_J/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6631, -193, 7434, 1
                }
                name: string = "LevelProp_brush_HA_J30"
            }
            0xc50df487 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6553.29394, -193, 7261.29394 }
                boxMax: vec3 = { 6702.70605, 79.0877991, 7410.70605 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6628, -193, 7336, 1
                }
                name: string = "LevelProp_brush_HA_E45"
            }
            0x009ac27b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4235.78857, -194.97287, 5255.78857 }
                boxMax: vec3 = { 4366.21142, -26.9770966, 5386.21142 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4301, -193, 5321, 1
                }
                name: string = "LevelProp_brush_HA_G27"
            }
            0x5a54f14b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6445.29394, -193, 7093.29394 }
                boxMax: vec3 = { 6594.70605, 79.0877991, 7242.70605 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6520, -193, 7168, 1
                }
                name: string = "LevelProp_brush_HA_E43"
            }
            0x4eb3af51 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5617.63672, -216, 6115.63672 }
                boxMax: vec3 = { 5760.36328, 69.2662048, 6258.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5689, -216, 6187, 1
                }
                name: string = "LevelProp_brush_HA_D30"
            }
            0x5355f5f4 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5851.6831, -740.912292, 7595.6831 }
                boxMax: vec3 = { 5932.31689, -691.541931, 7676.31689 }
                0xad304db5: string = "Characters/HA_AP_Poro/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.707106769, 0, 0.707106769, 0
                    0, 1, 0, 0
                    -0.707106769, 0, -0.707106769, 0
                    5892, -742, 7636, 1
                }
                name: string = "LevelProp_HA_AP_Poro2"
            }
            0xb75411ce = GdsMapObject {
                type: u8 = 9
                boxMin: vec3 = { 5890.98193, -275.068085, 5151.98193 }
                boxMax: vec3 = { 5967.01807, -193, 5228.01807 }
                0xad304db5: string = "Characters/SightWard/Skins/Skin0"
                sceneLayer: string = "Info Points"
                transform: mtx44 = {
                    0.829382002, 0, 0, 0
                    0, -0.829382002, -1.01570004e-16, 0
                    0, 1.01570004e-16, -0.829382002, 0
                    5929, -193, 5190, 1
                }
                name: string = "Info_HealthPack01"
            }
            0xfd50ab53 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6782.80859, 15.493825, 5438.80176 }
                boxMax: vec3 = { 6884.68896, 111.683212, 5541.9668 }
                0xad304db5: string = "Characters/HA_AP_Poro_Large/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.0104393614, -0.124775834, 0.992130041, 0
                    -0.0928491727, 0.987776637, 0.125205308, 0
                    -0.995625436, -0.0934255123, -0.00127357617, 0
                    6837, 29, 5486, 1
                }
                name: string = "LevelProp_HA_AP_Poro_Large"
            }
            0xfeb17a57 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4008.9458, -201.904572, 4887.9458 }
                boxMax: vec3 = { 4059.0542, -137.444687, 4938.0542 }
                0xad304db5: string = "Characters/brush_HA_I/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.472158998, 0, 0, 0
                    0, 0.472158998, 0, 0
                    0, 0, 0.472158998, 0
                    4034, -193, 4913, 1
                }
                name: string = "LevelProp_brush_HA_I18"
            }
            0xb4dbe2b4 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 3997.3479, -193, 5079.34766 }
                boxMax: vec3 = { 4106.65234, -72.1799011, 5188.65234 }
                0xad304db5: string = "Characters/brush_HA_J/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4052, -193, 5134, 1
                }
                name: string = "LevelProp_brush_HA_J17"
            }
            0x4a3e3134 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5470.29394, -193, 6211.29394 }
                boxMax: vec3 = { 5619.70605, 79.0877991, 6360.70605 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5545, -193, 6286, 1
                }
                name: string = "LevelProp_brush_HA_E29"
            }
            0x34faa6c3 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6417.93701, -211.859253, 7222.93701 }
                boxMax: vec3 = { 6524.06299, -75.3377075, 7329.06299 }
                0xad304db5: string = "Characters/brush_HA_I/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6471, -193, 7276, 1
                }
                name: string = "LevelProp_brush_HA_I33"
            }
            0xb0bb7796 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6308.70361, -199.082001, 6768.70361 }
                boxMax: vec3 = { 6347.29639, -86.8568039, 6807.29639 }
                0xad304db5: string = "Characters/brush_HA_H/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6328, -199, 6788, 1
                }
                name: string = "LevelProp_brush_HA_H31"
            }
            0x34366c9e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5456.78857, -194.97287, 6119.78857 }
                boxMax: vec3 = { 5587.21142, -26.9770966, 6250.21142 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5522, -193, 6185, 1
                }
                name: string = "LevelProp_brush_HA_G28"
            }
            0xe88eb10a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7935.70361, -193.082001, 8670.70312 }
                boxMax: vec3 = { 7974.29639, -80.8568039, 8709.29688 }
                0xad304db5: string = "Characters/brush_HA_H/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7955, -193, 8690, 1
                }
                name: string = "LevelProp_brush_HA_H26"
            }
            0x95c3062d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6365.78857, -194.97287, 7186.78857 }
                boxMax: vec3 = { 6496.21142, -26.9770966, 7317.21142 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6431, -193, 7252, 1
                }
                name: string = "LevelProp_brush_HA_G45"
            }
            0x229145e0 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6291.54932, -197.79007, 6901.54932 }
                boxMax: vec3 = { 6484.45068, 0.0973052979, 7094.45068 }
                0xad304db5: string = "Characters/brush_HA_B/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.939692616, 0, 0.342020124, 0
                    0, 1, 0, 0
                    -0.342020124, 0, 0.939692616, 0
                    6388, -193, 6998, 1
                }
                name: string = "LevelProp_brush_HA_B34"
            }
            0x73e64aa6 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6415.74854, -197.79007, 7293.74854 }
                boxMax: vec3 = { 6566.25146, 0.0973052979, 7444.25146 }
                0xad304db5: string = "Characters/brush_HA_B/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6491, -193, 7369, 1
                }
                name: string = "LevelProp_brush_HA_B35"
            }
            0xfb7ec490 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6504.74854, -197.79007, 7122.74854 }
                boxMax: vec3 = { 6655.25146, 0.0973052979, 7273.25146 }
                0xad304db5: string = "Characters/brush_HA_B/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6580, -193, 7198, 1
                }
                name: string = "LevelProp_brush_HA_B36"
            }
            0xab661f31 = GdsMapObject {
                type: u8 = 1
                boxMin: vec3 = { 11793.6084, -114, 11529.6084 }
                boxMax: vec3 = { 11926.3916, 169.725891, 11662.3916 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    11860, -114, 11596, 1
                }
                name: string = "__Spawn_T2"
            }
            0xfdfc81a9 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6536.63672, -193, 7194.63672 }
                boxMax: vec3 = { 6679.36328, 92.2662048, 7337.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6608, -193, 7266, 1
                }
                name: string = "LevelProp_brush_HA_D43"
            }
            0x1d3f3497 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 6750.33398, -111.289566, 6678.33398 }
                boxMax: vec3 = { 6853.66602, -5.95820618, 6781.66602 }
                0xad304db5: string = "Characters/ThreshLantern/Skins/Skin0"
                sceneLayer: string = "Nav Points"
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    6802, -160, 6730, 1
                }
                name: string = "__NAV_C010"
            }
            0xd1542fd2 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4203.37646, -193.75737, 5255.37646 }
                boxMax: vec3 = { 4336.62354, 31.9250336, 5388.62354 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.77333802, 0, 0, 0
                    0, 0.77333802, 0, 0
                    0, 0, 0.77333802, 0
                    4270, -193, 5322, 1
                }
                name: string = "LevelProp_brush_HA_A30"
            }
            0xcede2027 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6525.34766, -193, 7360.34766 }
                boxMax: vec3 = { 6634.65234, -72.1799011, 7469.65234 }
                0xad304db5: string = "Characters/brush_HA_J/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6580, -193, 7415, 1
                }
                name: string = "LevelProp_brush_HA_J29"
            }
            0xeeb40863 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7848.78857, -194.97287, 8627.78906 }
                boxMax: vec3 = { 7979.21142, -26.9770966, 8758.21094 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7914, -193, 8693, 1
                }
                name: string = "LevelProp_brush_HA_G39"
            }
            0x725cb108 = GdsMapObject {
                type: u8 = 9
                boxMin: vec3 = { 11272.9824, -347.068085, 10990.9824 }
                boxMax: vec3 = { 11349.0176, -265, 11067.0176 }
                0xad304db5: string = "Characters/SightWard/Skins/Skin0"
                sceneLayer: string = "Info Points"
                transform: mtx44 = {
                    0.829382002, 0, 0, 0
                    0, -0.829382002, -1.01570004e-16, 0
                    0, 1.01570004e-16, -0.829382002, 0
                    11311, -265, 11029, 1
                }
                name: string = "Info_ChaosRandomThingy01"
            }
            0x6df9a9e7 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 3923.01709, -195.875198, 4871.01709 }
                boxMax: vec3 = { 4046.98291, -36.1960602, 4994.98291 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.950495005, 0, 0, 0
                    0, 0.950495005, 0, 0
                    0, 0, 0.950495005, 0
                    3985, -194, 4933, 1
                }
                name: string = "LevelProp_brush_HA_G25"
            }
            0x2d1ec345 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5573.29394, -196, 6074.29394 }
                boxMax: vec3 = { 5722.70605, 76.0877991, 6223.70605 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5648, -196, 6149, 1
                }
                name: string = "LevelProp_brush_HA_E31"
            }
            0x4d596c49 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5303.00537, -193.307343, 6070.00537 }
                boxMax: vec3 = { 5438.99463, 54.3355103, 6205.99463 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5371, -193, 6138, 1
                }
                name: string = "LevelProp_brush_HA_F30"
            }
            0xc5c58411 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6393.84912, -193.97934, 7029.84912 }
                boxMax: vec3 = { 6566.15088, 97.8495789, 7202.15088 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6480, -193, 7116, 1
                }
                name: string = "LevelProp_brush_HA_A48"
            }
            0x82a4297f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5531.71387, -193, 6199.71387 }
                boxMax: vec3 = { 5686.28613, 82.9436951, 6354.28613 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.851311028, 0, 0, 0
                    0, 0.851311028, 0, 0
                    0, 0, 0.851311028, 0
                    5609, -193, 6277, 1
                }
                name: string = "LevelProp_brush_HA_C26"
            }
            0x15569265 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 3913.06689, -193, 4859.06689 }
                boxMax: vec3 = { 4042.9331, 38.8386536, 4988.9331 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.715242982, 0, 0, 0
                    0, 0.715242982, 0, 0
                    0, 0, 0.715242982, 0
                    3978, -193, 4924, 1
                }
                name: string = "LevelProp_brush_HA_C23"
            }
            0xe3972ef5 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5870.34766, -216, 6269.34766 }
                boxMax: vec3 = { 5979.65234, -95.1799011, 6378.65234 }
                0xad304db5: string = "Characters/brush_HA_J/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5925, -216, 6324, 1
                }
                name: string = "LevelProp_brush_HA_J22"
            }
            0x1d62fb5d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7596.76807, -193.267731, 8279.76855 }
                boxMax: vec3 = { 7715.23193, 22.4608917, 8398.23144 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.871128023, 0, 0, 0
                    0, 0.871128023, 0, 0
                    0, 0, 0.871128023, 0
                    7656, -193, 8339, 1
                }
                name: string = "LevelProp_brush_HA_F38"
            }
            0x0b5ffe3f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5774.78857, -194.97287, 6292.78857 }
                boxMax: vec3 = { 5905.21142, -26.9770966, 6423.21142 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5840, -193, 6358, 1
                }
                name: string = "LevelProp_brush_HA_G33"
            }
            0x59803189 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 3961.41797, -215.057724, 4893.41797 }
                boxMax: vec3 = { 3988.58203, -136.066666, 4920.58203 }
                0xad304db5: string = "Characters/brush_HA_H/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.703862011, 0, 0, 0
                    0, 0.703862011, 0, 0
                    0, 0, 0.703862011, 0
                    3975, -215, 4907, 1
                }
                name: string = "LevelProp_brush_HA_H17"
            }
            0x5e2bbc12 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 3882.65137, -193.833817, 4913.65137 }
                boxMax: vec3 = { 4029.34863, 54.6284485, 5060.34863 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.851396978, 0, 0, 0
                    0, 0.851396978, 0, 0
                    0, 0, 0.851396978, 0
                    3956, -193, 4987, 1
                }
                name: string = "LevelProp_brush_HA_A"
            }
            0x60a72dbe = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 3611.33398, -105.289566, 4075.33398 }
                boxMax: vec3 = { 3714.66602, 0.0417938232, 4178.66602 }
                0xad304db5: string = "Characters/ThreshLantern/Skins/Skin0"
                sceneLayer: string = "Nav Points"
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    3663, -154, 4127, 1
                }
                name: string = "__NAV_C04"
            }
            0xa101e94a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7491.68701, -193.073578, 8346.6875 }
                boxMax: vec3 = { 7526.31299, -92.3842316, 8381.3125 }
                0xad304db5: string = "Characters/brush_HA_H/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.897207975, 0, 0, 0
                    0, 0.897207975, 0, 0
                    0, 0, 0.897207975, 0
                    7509, -193, 8364, 1
                }
                name: string = "LevelProp_brush_HA_H24"
            }
            0x174b3af6 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7602.34766, -193, 8502.34766 }
                boxMax: vec3 = { 7711.65234, -72.1799011, 8611.65234 }
                0xad304db5: string = "Characters/brush_HA_J/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7657, -193, 8557, 1
                }
                name: string = "LevelProp_brush_HA_J25"
            }
            0x92c3a97f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5879.29394, -213, 6279.29394 }
                boxMax: vec3 = { 6028.70605, 59.0877991, 6428.70605 }
                0xad304db5: string = "Characters/brush_HA_E/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5954, -213, 6354, 1
                }
                name: string = "LevelProp_brush_HA_E33"
            }
            0x4a6b1d93 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 3962.84912, -193.97934, 4901.84912 }
                boxMax: vec3 = { 4135.15088, 97.8495789, 5074.15088 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4049, -193, 4988, 1
                }
                name: string = "LevelProp_brush_HA_A28"
            }
            0x0ea777fe = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4276.21533, -193, 5128.21533 }
                boxMax: vec3 = { 4457.78467, 131.139709, 5309.78467 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4367, -193, 5219, 1
                }
                name: string = "LevelProp_brush_HA_C24"
            }
            0x9bdaa972 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5616.74854, -197.79007, 6253.74854 }
                boxMax: vec3 = { 5767.25146, 0.0973052979, 6404.25146 }
                0xad304db5: string = "Characters/brush_HA_B/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5692, -193, 6329, 1
                }
                name: string = "LevelProp_brush_HA_B26"
            }
            0x8befd58f = GdsMapObject {
                type: u8 = 4
                boxMin: vec3 = { 10561.041, -997.899414, 10349.7236 }
                boxMax: vec3 = { 11311.2637, 171.910843, 11099.9463 }
                0xad304db5: string = "Characters/ChaosNexus/Skins/Skin1"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.156434596, 0, 0.987688303, 0
                    0, 1, 0, 0
                    -0.987688303, 0, 0.156434596, 0
                    10936, -180, 10724, 1
                }
                name: string = "HQ_T2"
            }
            0x2fd44fcf = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6550.21533, -193, 7205.21533 }
                boxMax: vec3 = { 6731.78467, 131.139709, 7386.78467 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6641, -193, 7296, 1
                }
                name: string = "LevelProp_brush_HA_C40"
            }
            0xc45ac0c2 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6523.00537, -193.307343, 7019.00537 }
                boxMax: vec3 = { 6658.99463, 54.3355103, 7154.99463 }
                0xad304db5: string = "Characters/brush_HA_F/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6591, -193, 7087, 1
                }
                name: string = "LevelProp_brush_HA_F45"
            }
            0x3f07604c = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 8691.33398, -125.289566, 8933.33398 }
                boxMax: vec3 = { 8794.66602, -19.9582062, 9036.66602 }
                0xad304db5: string = "Characters/ThreshLantern/Skins/Skin0"
                sceneLayer: string = "Nav Points"
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    8743, -174, 8985, 1
                }
                name: string = "__NAV_C014"
            }
            0xdd90f153 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4246.78857, -194.97287, 5079.78857 }
                boxMax: vec3 = { 4377.21142, -26.9770966, 5210.21142 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4312, -193, 5145, 1
                }
                name: string = "LevelProp_brush_HA_G26"
            }
            0xb7c64786 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5300.78857, -194.97287, 6144.78857 }
                boxMax: vec3 = { 5431.21142, -26.9770966, 6275.21142 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5366, -193, 6210, 1
                }
                name: string = "LevelProp_brush_HA_G29"
            }
            0x2ca6001e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5565.21533, -193, 6217.21533 }
                boxMax: vec3 = { 5746.78467, 131.139709, 6398.78467 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5656, -193, 6308, 1
                }
                name: string = "LevelProp_brush_HA_C30"
            }
            0xcdb5d18e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 396.794098, 717.657715, 531.049072 }
                boxMax: vec3 = { 479.84491, 784.408813, 620.923828 }
                0xad304db5: string = "Characters/HA_AP_Poro/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.714005232, 0.198216364, -0.671495974, 0
                    0.05119735, 0.971301436, 0.23227641, 0
                    0.69826597, 0.131467745, -0.703662455, 0
                    437, 726, 570, 1
                }
                name: string = "LevelProp_HA_AP_Poro"
            }
            0xef46e464 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7554.61133, -193, 8379.61133 }
                boxMax: vec3 = { 7713.38867, 90.4511108, 8538.38867 }
                0xad304db5: string = "Characters/brush_HA_C/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.874472022, 0, 0, 0
                    0, 0.874472022, 0, 0
                    0, 0, 0.874472022, 0
                    7634, -193, 8459, 1
                }
                name: string = "LevelProp_brush_HA_C33"
            }
            0x0b93eb9f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6280.63672, -193, 6725.63672 }
                boxMax: vec3 = { 6423.36328, 92.2662048, 6868.36328 }
                0xad304db5: string = "Characters/brush_HA_D/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6352, -193, 6797, 1
                }
                name: string = "LevelProp_brush_HA_D45"
            }
            0x7b80704d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5712.84912, -193.97934, 6202.84912 }
                boxMax: vec3 = { 5885.15088, 97.8495789, 6375.15088 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5799, -193, 6289, 1
                }
                name: string = "LevelProp_brush_HA_A37"
            }
            0xf2e5e481 = GdsMapObject {
                type: u8 = 1
                boxMin: vec3 = { 869.608398, -106, 993.608398 }
                boxMax: vec3 = { 1002.3916, 177.725891, 1126.3916 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    936, -106, 1060, 1
                }
                name: string = "__Spawn_T1"
            }
            0x04410461 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7631.65186, -193.822433, 8530.65137 }
                boxMax: vec3 = { 7776.34814, 51.2514038, 8675.34863 }
                0xad304db5: string = "Characters/brush_HA_A/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    0.839785993, 0, 0, 0
                    0, 0.839785993, 0, 0
                    0, 0, 0.839785993, 0
                    7704, -193, 8603, 1
                }
                name: string = "LevelProp_brush_HA_A39"
            }
            0x05fb0103 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6402.78857, -194.97287, 6992.78857 }
                boxMax: vec3 = { 6533.21142, -26.9770966, 7123.21142 }
                0xad304db5: string = "Characters/brush_HA_G/Skins/Skin0"
                sceneLayer: string = "Level Props"
                castStaticShadows: bool = true
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6468, -193, 7058, 1
                }
                name: string = "LevelProp_brush_HA_G40"
            }
            0x1884a50b = GdsMapObject {
                type: u8 = 6
                boxMin: vec3 = { 10488.1728, -187.462204, 11733.2324 }
                boxMax: vec3 = { 11633.8604, 0, 12879.7344 }
                0xad304db5: string = "Characters/sru_storekeepernorth/Skins/Skin0"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11065, -184, 12306, 1
                }
                name: string = "ChaosShop01"
            }
            0x972c947d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7043.49219, -932.366089, 5482.44336 }
                boxMax: vec3 = { 7223.13184, 0, 5662.0835 }
                0xad304db5: string = "Characters/HA_AP_BannerMidBridge/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.719339788, 0, 0.694658399, 0
                    0, 1, 0, 0
                    -0.694658399, 0, 0.719339788, 0
                    7088, -756, 5605, 1
                }
                name: string = "LevelProp_HA_AP_BannerMidBridge"
            }
            0x37b2e2ff = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4936.68213, -149.475906, 3406.52075 }
                boxMax: vec3 = { 5116.32226, 0, 3586.16089 }
                mapObjectSkinID: u32 = 1
                0xad304db5: string = "Characters/HA_AP_BridgeLaneStatue/Skins/Skin1"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.694658399, 0, -0.719339788, 0
                    0, 1, 0, 0
                    0.719339788, 0, -0.694658399, 0
                    4903, 92, 3607, 1
                }
                name: string = "LevelProp_HA_AP_BridgeLaneStatue1"
            }
            0x459a7bc5 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6376.35205, -130.654205, 4770.47852 }
                boxMax: vec3 = { 6555.99219, 0, 4950.11865 }
                mapObjectSkinID: u32 = 1
                0xad304db5: string = "Characters/HA_AP_BridgeLaneStatue/Skins/Skin1"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.694658399, 0, -0.719339788, 0
                    0, 1, 0, 0
                    0.719339788, 0, -0.694658399, 0
                    6321, 89, 5004, 1
                }
                name: string = "LevelProp_HA_AP_BridgeLaneStatue2"
            }
            0x8024d8d2 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7809.47949, -134.860703, 6154.30908 }
                boxMax: vec3 = { 7989.11963, 0, 6333.94971 }
                mapObjectSkinID: u32 = 1
                0xad304db5: string = "Characters/HA_AP_BridgeLaneStatue/Skins/Skin1"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.719339788, 0, -0.694658399, 0
                    0, 1, 0, 0
                    0.694658399, 0, -0.719339788, 0
                    7776, 84, 6377, 1
                }
                name: string = "LevelProp_HA_AP_BridgeLaneStatue3"
            }
            0xf9cce6da = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9232.81641, -128.451004, 7528.68652 }
                boxMax: vec3 = { 9412.45605, 0, 7708.32666 }
                mapObjectSkinID: u32 = 1
                0xad304db5: string = "Characters/HA_AP_BridgeLaneStatue/Skins/Skin1"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.694658399, 0, -0.719339788, 0
                    0, 1, 0, 0
                    0.719339788, 0, -0.694658399, 0
                    9188, 80, 7740, 1
                }
                name: string = "LevelProp_HA_AP_BridgeLaneStatue4"
            }
            0xadb6bc5a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7718.02051, -130.713898, 9145.54004 }
                boxMax: vec3 = { 7897.65918, 0, 9325.17969 }
                mapObjectSkinID: u32 = 1
                0xad304db5: string = "Characters/HA_AP_BridgeLaneStatue/Skins/Skin1"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.719339788, 0, 0.694658399, 0
                    0, 1, 0, 0
                    -0.694658399, 0, 0.719339788, 0
                    7918, 78, 9123, 1
                }
                name: string = "LevelProp_HA_AP_BridgeLaneStatue5"
            }
            0x0e4fedbd = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6255.11426, -131.104401, 7812.15478 }
                boxMax: vec3 = { 6434.75391, 0, 7991.79394 }
                mapObjectSkinID: u32 = 1
                0xad304db5: string = "Characters/HA_AP_BridgeLaneStatue/Skins/Skin1"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.719339788, 0, 0.694658399, 0
                    0, 1, 0, 0
                    -0.694658399, 0, 0.719339788, 0
                    6488, 88, 7745, 1
                }
                name: string = "LevelProp_HA_AP_BridgeLaneStatue6"
            }
            0x1e275206 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4821.58447, -133.031693, 6429.22363 }
                boxMax: vec3 = { 5001.22461, 0, 6608.86426 }
                mapObjectSkinID: u32 = 1
                0xad304db5: string = "Characters/HA_AP_BridgeLaneStatue/Skins/Skin1"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.74314481, 0, 0.669130623, 0
                    0, 1, 0, 0
                    -0.669130623, 0, 0.74314481, 0
                    5055, 86, 6352, 1
                }
                name: string = "LevelProp_HA_AP_BridgeLaneStatue7"
            }
            0xb6f3dc5b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 3398.83936, -132.129807, 5054.12988 }
                boxMax: vec3 = { 3578.47974, 0, 5233.77002 }
                mapObjectSkinID: u32 = 1
                0xad304db5: string = "Characters/HA_AP_BridgeLaneStatue/Skins/Skin1"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.719339788, 0, 0.694658399, 0
                    0, 1, 0, 0
                    -0.694658399, 0, 0.719339788, 0
                    3632, 87, 4998, 1
                }
                name: string = "LevelProp_HA_AP_BridgeLaneStatue8"
            }
            0xabdad6b6 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 3863.62964, -198.009399, 6079.40625 }
                boxMax: vec3 = { 4043.27002, 0, 6259.0459 }
                0xad304db5: string = "Characters/HA_AP_Chains/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.694658399, 0, 0.719339788, 0
                    0, 1, 0, 0
                    -0.719339788, 0, 0.694658399, 0
                    3930, 88, 6102, 1
                }
                name: string = "LevelProp_HA_AP_Chains1"
            }
            0x392a70df = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5247.37109, -198.009399, 7415.5498 }
                boxMax: vec3 = { 5427.01074, 0, 7595.18896 }
                0xad304db5: string = "Characters/HA_AP_Chains/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.719339788, 0, 0.694658399, 0
                    0, 1, 0, 0
                    -0.694658399, 0, 0.719339788, 0
                    5348, 77, 7505, 1
                }
                name: string = "LevelProp_HA_AP_Chains2"
            }
            0x6da38c26 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6714.43652, -198.009399, 8832.15137 }
                boxMax: vec3 = { 6894.07666, 0, 9011.79102 }
                0xad304db5: string = "Characters/HA_AP_Chains/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.719339788, 0, 0.694658399, 0
                    0, 1, 0, 0
                    -0.694658399, 0, 0.719339788, 0
                    6770, 66, 8887, 1
                }
                name: string = "LevelProp_HA_AP_Chains3"
            }
            0x48174e63 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7424.88184, -198.009399, 5138.11035 }
                boxMax: vec3 = { 7604.52197, 0, 5317.75049 }
                0xad304db5: string = "Characters/HA_AP_Chains/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.766044438, 0, 0.642787635, 0
                    0, 1, 0, 0
                    -0.642787635, 0, 0.766044438, 0
                    7491, 77, 5249, 1
                }
                name: string = "LevelProp_HA_AP_Chains4"
            }
            0xfa5a1d2f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8903.12012, -198.009399, 6565.5 }
                boxMax: vec3 = { 9082.75976, 0, 6745.13916 }
                0xad304db5: string = "Characters/HA_AP_Chains/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.719339788, 0, 0.694658399, 0
                    0, 1, 0, 0
                    -0.694658399, 0, 0.719339788, 0
                    8958, 88, 6577, 1
                }
                name: string = "LevelProp_HA_AP_Chains5"
            }
            0x533313cd = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6062.79541, -198.009399, 3822.87695 }
                boxMax: vec3 = { 6242.43604, 0, 4002.51709 }
                0xad304db5: string = "Characters/HA_AP_Chains/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.74314481, 0, 0.669130623, 0
                    0, 1, 0, 0
                    -0.669130623, 0, 0.74314481, 0
                    6074, 88, 3867, 1
                }
                name: string = "LevelProp_HA_AP_Chains6"
            }
            0xf725334e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 2882.27808, -333.180695, 5183.78564 }
                boxMax: vec3 = { 3061.91846, 0, 5363.42627 }
                0xad304db5: string = "Characters/HA_AP_Chains_Long/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.809017003, 0, 0.587785244, 0
                    0, 1, 0, 0
                    -0.587785244, 0, 0.809017003, 0
                    2883, 86, 5173, 1
                }
                name: string = "LevelProp_HA_AP_Chains_Long"
            }
            0x19de1bb0 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9739.00488, -294.200409, 7650.02588 }
                boxMax: vec3 = { 9918.64551, 0, 7829.6665 }
                0xad304db5: string = "Characters/HA_AP_Chains_Long/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.766044438, 0, 0.642787635, 0
                    0, 1, 0, 0
                    -0.642787635, 0, 0.766044438, 0
                    9939, 70, 7627, 1
                }
                name: string = "LevelProp_HA_AP_Chains_Long1"
            }
            0x9b191a3c = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4894.2373, -333.180695, 3034.15283 }
                boxMax: vec3 = { 5073.87793, 0, 3213.79346 }
                0xad304db5: string = "Characters/HA_AP_Chains_Long/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.694658399, 0, 0.719339788, 0
                    0, 1, 0, 0
                    -0.719339788, 0, 0.694658399, 0
                    5139, 97, 2800, 1
                }
                name: string = "LevelProp_HA_AP_Chains_Long2"
            }
            0xe39a0aea = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7667.979, -333.180695, 9612.71484 }
                boxMax: vec3 = { 7847.61865, 0, 9792.35547 }
                0xad304db5: string = "Characters/HA_AP_Chains_Long/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.694658399, 0, 0.719339788, 0
                    0, 1, 0, 0
                    -0.719339788, 0, 0.694658399, 0
                    7723, 86, 9868, 1
                }
                name: string = "LevelProp_HA_AP_Chains_Long3"
            }
            0x181dd3a7 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8447.87305, -463.711487, 7183.45459 }
                boxMax: vec3 = { 8627.51172, 0, 7363.09375 }
                0xad304db5: string = "Characters/HA_AP_Cutaway/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.694658399, 0, 0.719339788, 0
                    0, 1, 0, 0
                    -0.719339788, 0, 0.694658399, 0
                    7814, -221, 7517, 1
                }
                name: string = "LevelProp_HA_AP_Cutaway"
            }
            0x501864a2 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 11103.5723, -227.564896, 11980.9316 }
                boxMax: vec3 = { 11156.1406, 0, 12033.502 }
                0xad304db5: string = "Characters/HA_AP_Hermit/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.719339788, 0, -0.694658399, 0
                    0, 1, 0, 0
                    0.694658399, 0, -0.719339788, 0
                    11217, -163, 12037, 1
                }
                name: string = "LevelProp_HA_AP_Hermit"
            }
            0x55dcf159 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 11103.5723, -227.564896, 11980.9316 }
                boxMax: vec3 = { 11156.1406, 0, 12033.502 }
                0xad304db5: string = "Characters/HA_AP_Hermit_Robot/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.939692616, 0, -0.342020154, 0
                    0, 1, 0, 0
                    0.342020154, 0, -0.939692616, 0
                    11195, -208, 12129, 1
                }
                name: string = "LevelProp_HA_AP_Hermit_Robot1"
            }
            0xaed1352e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 1547.87085, -3049.82666, 5989.85547 }
                boxMax: vec3 = { 1727.51099, 0, 6169.49609 }
                0xad304db5: string = "Characters/HA_AP_HeroTower/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.719339788, 0, 0.694658399, 0
                    0, 1, 0, 0
                    -0.694658399, 0, 0.719339788, 0
                    1637, -3986, 6079, 1
                }
                name: string = "LevelProp_HA_AP_HeroTower"
            }
            0x54e6352f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { -277.34729, -8929.56738, 16894.4492 }
                boxMax: vec3 = { 499.179413, 0, 17670.9746 }
                mapObjectSkinID: u32 = 1
                0xad304db5: string = "Characters/HA_AP_PeriphBridge/Skins/Skin1"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.898794055, 0, 0.438371152, 0
                    0, 1, 0, 0
                    -0.438371152, 0, 0.898794055, 0
                    -501, -8218, 17370, 1
                }
                name: string = "LevelProp_HA_AP_PeriphBridge"
            }
            0xeeca6b84 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10979.6318, -137.418503, 12079.6308 }
                boxMax: vec3 = { 11066.0644, 0, 12166.0635 }
                0xad304db5: string = "Characters/HA_AP_ShpNorth/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.37460658, 0, 0.927183867, 0
                    0, 1, 0, 0
                    -0.927183867, 0, 0.37460658, 0
                    10810, -217, 11977, 1
                }
                name: string = "LevelProp_HA_AP_ShpNorth"
            }
            0x92933e48 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 436.738098, -221.540207, 1884.09436 }
                boxMax: vec3 = { 472.355591, 0, 1919.71252 }
                0xad304db5: string = "Characters/HA_AP_ShpSouth/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.719339788, 0, 0.694658399, 0
                    0, 1, 0, 0
                    -0.694658399, 0, 0.719339788, 0
                    520, -185, 1912, 1
                }
                name: string = "LevelProp_HA_AP_ShpSouth"
            }
            0xe956ccb4 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 420.223511, -221.540405, 1879.13672 }
                boxMax: vec3 = { 455.841003, 0, 1914.75488 }
                0xad304db5: string = "Characters/HA_AP_Viking/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.642787635, 0, -0.766044438, 0
                    0, 1, 0, 0
                    0.766044438, 0, -0.642787635, 0
                    515, -96, 1918, 1
                }
                name: string = "LevelProp_HA_AP_Viking"
            }
            0x10dd24c5 = GdsMapObject {
                type: u8 = 6
                boxMin: vec3 = { 103.280403, -444.573792, 1547.81775 }
                boxMax: vec3 = { 890.844604, 364.829712, 2317.48584 }
                0xad304db5: string = "Characters/sru_storekeepernorth/Skins/Skin0"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    491, -111, 1949, 1
                }
                name: string = "OrderShop01"
            }
            0xbc83526d = GdsMapObject {
                type: u8 = 5
                boxMin: vec3 = { 12121.748, -124.417198, 11866.3105 }
                boxMax: vec3 = { 12215.7051, 0, 11945.4102 }
                0xad304db5: string = "Characters/HA_AP_ChaosTurret/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.694658399, 0, -0.719339788, 0
                    0, 1, 0, 0
                    0.719339788, 0, 0.694658399, 0
                    12183, 27, 11844, 1
                }
                name: string = "Turret_ChaosTurretShrine"
            }
            0xf4af88d5 = GdsMapObject {
                type: u8 = 5
                boxMin: vec3 = { 601.112915, -124.417099, 717.248413 }
                boxMax: vec3 = { 695.07019, 0, 796.348328 }
                0xad304db5: string = "Characters/HA_AP_OrderTurret/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.642787635, 0, 0.766044438, 0
                    0, 1, 0, 0
                    -0.766044438, 0, -0.642787635, 0
                    648, -150, 764, 1
                }
                name: string = "Turret_OrderTurretShrine"
            }
            0x7a388fdf = GdsMapObject {
                type: u8 = 5
                boxMin: vec3 = { 1979.76367, -179.283798, 2495.78784 }
                boxMax: vec3 = { 2093.54907, 0, 2609.57446 }
                0xad304db5: string = "Characters/HA_AP_OrderTurret/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.669130623, 0, 0.74314481, 0
                    0, 1, 0, 0
                    -0.74314481, 0, -0.669130623, 0
                    2051, -179, 2560, 1
                }
                name: string = "Turret_T1_C_010"
            }
            0x7c2dca94 = GdsMapObject {
                type: u8 = 5
                boxMin: vec3 = { 3762.08252, -155.493301, 3782.07226 }
                boxMax: vec3 = { 3856.03955, 0, 3876.03052 }
                0xad304db5: string = "Characters/HA_AP_OrderTurret/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.694658399, 0, 0.719339788, 0
                    0, 1, 0, 0
                    -0.719339788, 0, -0.694658399, 0
                    3809, -155, 3829, 1
                }
                name: string = "Turret_T1_C_07"
            }
            0xc842faa8 = GdsMapObject {
                type: u8 = 5
                boxMin: vec3 = { 4896.5, -159.769897, 4882.84131 }
                boxMax: vec3 = { 4990.45605, 0, 4976.79785 }
                0xad304db5: string = "Characters/HA_AP_OrderTurret/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.694658399, 0, 0.719339788, 0
                    0, 1, 0, 0
                    -0.719339788, 0, -0.694658399, 0
                    4943, -159, 4929, 1
                }
                name: string = "Turret_T1_C_08"
            }
            0x40745606 = GdsMapObject {
                type: u8 = 5
                boxMin: vec3 = { 2436.33984, -182.657303, 2044.28845 }
                boxMax: vec3 = { 2550.12305, 0, 2158.07275 }
                0xad304db5: string = "Characters/HA_AP_OrderTurret/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.669130623, 0, 0.74314481, 0
                    0, 1, 0, 0
                    -0.74314481, 0, -0.669130623, 0
                    2493, -182, 2101, 1
                }
                name: string = "Turret_T1_C_09"
            }
            0xcc783df8 = GdsMapObject {
                type: u8 = 5
                boxMin: vec3 = { 7829.99512, -159.114197, 7725.69629 }
                boxMax: vec3 = { 7928.20947, 0, 7823.90723 }
                0xad304db5: string = "Characters/HA_AP_ChaosTurret/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.694658399, 0, -0.719339788, 0
                    0, 1, 0, 0
                    0.719339788, 0, 0.694658399, 0
                    7883, -159, 7767, 1
                }
                name: string = "Turret_T2_L_01"
            }
            0xaf7d7fd7 = GdsMapObject {
                type: u8 = 5
                boxMin: vec3 = { 8968.52246, -161.747498, 8822.25586 }
                boxMax: vec3 = { 9066.73633, 0, 8920.4668 }
                0xad304db5: string = "Characters/HA_AP_ChaosTurret/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.694658399, 0, -0.719339788, 0
                    0, 1, 0, 0
                    0.719339788, 0, 0.694658399, 0
                    9017, -161, 8871, 1
                }
                name: string = "Turret_T2_L_02"
            }
            0xbad9cca8 = GdsMapObject {
                type: u8 = 5
                boxMin: vec3 = { 10736.0693, -169.333298, 10068.4824 }
                boxMax: vec3 = { 10834.2832, 0, 10166.6924 }
                0xad304db5: string = "Characters/HA_AP_ChaosTurret/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.669130623, 0, -0.74314481, 0
                    0, 1, 0, 0
                    0.74314481, 0, 0.669130623, 0
                    10785, -169, 10117, 1
                }
                name: string = "Turret_T2_L_03"
            }
            0xf9d8c9aa = GdsMapObject {
                type: u8 = 5
                boxMin: vec3 = { 10276.1152, -177.966599, 10559.0928 }
                boxMax: vec3 = { 10374.3291, 0, 10657.3037 }
                0xad304db5: string = "Characters/HA_AP_ChaosTurret/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    0.694658399, 0, -0.719339788, 0
                    0, 1, 0, 0
                    0.719339788, 0, 0.694658399, 0
                    10353, -177, 10574, 1
                }
                name: string = "Turret_T2_L_04"
            }
            0x5be30813 = null
            0xba8d79d2 = null
            0x1c742ad9 = null
            0x4d8f2efc = null
            0x60f50b58 = null
            0x37d87b8e = null
            0x48436329 = null
            0xcaea5957 = null
            0x460ef287 = null
            0x98b50363 = null
            0x56ee9189 = null
            0xf3ed96f8 = null
            0x8a60e286 = null
            0xf989e6eb = null
            0x6ffac653 = null
            0xe0a3b5ad = null
            0x975a8f9b = null
            0xd986431c = null
            0x91959ce1 = null
            0xb4e73004 = null
            0xc6120344 = null
            0xd69fe743 = null
            0xc18e388e = null
            0x0d8b948b = null
            0x6e266024 = null
            0xe9da25b8 = null
            0xbe30f48c = null
            0xbdc51619 = null
            0xc1535f12 = null
            0xc812fee2 = null
            0xcd21b32a = null
            0x67cbd384 = null
            0x8b153766 = null
            0x5ff812a0 = null
            0x67f26a61 = null
            0xf933fe4d = null
            0x32a1ee96 = null
            0x5d271f11 = null
            0x4199b2db = null
            0x7e2bed9c = null
            0x10664986 = null
            0xe93fdfa7 = null
            0xa8451e56 = null
            0xaea2847e = null
            0x97efbcf0 = null
            0x1a9f1414 = null
            0xc167b5f5 = null
            0x55f90538 = null
            0xdda4bc62 = null
            0x0ff5e617 = null
            0xc81796bc = null
            0x201e9d78 = null
            0x814959ff = null
            0x139c367f = null
            0xa77e1746 = null
            0xec583a06 = null
            0x4a4ba99a = null
            0x6df7ab0f = null
            0xc6a298aa = null
            0x6b1f22b2 = null
            0x915e8bd0 = null
            0xa4a9c595 = null
            0x4824e488 = null
            0xa9c5c567 = null
            0xc78cd474 = null
            0x44eee44e = null
            0x5910220d = null
            0x993aa6e0 = null
            0xd5188e32 = null
            0xca7f5caf = null
            0xd30a0d82 = null
            0x057dea60 = null
            0x49a4dfcc = null
            0x261a4008 = null
            0x4930daec = null
            0x0e563a78 = null
            0xfb4c8e40 = null
            0xdb9159cb = null
            0xcf3a6b07 = null
            0x0ff0f77e = null
            0xe2aef8c2 = null
            0xf1a9d485 = null
            0x0ba82b31 = null
            0x30908878 = null
            0xe3629e00 = null
            0x3967ba0d = null
            0x926fa4b9 = null
            0x346ad51e = null
            0xa8779198 = null
            0xc33aef62 = null
            0x41356590 = null
            0xdf71ae35 = null
            0xd9b35144 = null
            0xef850e82 = null
            0x004c9648 = null
            0x5664c697 = null
            0x89bdda1f = null
            0xcc141d77 = null
            0x60d888cc = null
            0x0e628b9b = null
            0xc03721f7 = null
            0x0dc9ea13 = null
            0xf32e943f = null
            0x3624d100 = null
            0xcd9948e4 = null
            0xe9962a2f = null
            0x71e3716f = null
            0xc1ec8c78 = null
            0xd7072f2c = null
            0x9877ae46 = null
            0x02a190a1 = null
            0x7f0fc868 = null
            0x2f89997a = null
            0x9f685043 = null
            0xdb571a8d = null
            0xb848f786 = null
            0xfbbb9995 = null
            0xff49af6c = null
            0x65baa34f = null
            0x0e15b6a3 = null
            0x9896b827 = null
            0x87362795 = null
            0x683bcbac = null
            0x4e8e7763 = null
            0x987fc460 = null
            0x5ed0d86c = null
            0x726578b0 = null
            0xf3f8d69d = null
            0x328de430 = null
            0x36dbcb69 = null
            0x6f8845e5 = null
            0x7d4f6717 = null
            0x392b9fc1 = null
            0x0a67fac6 = null
            0xa43fa00d = null
            0xaa9a5d58 = null
            0x099d5cd8 = null
            0x843b57b1 = null
            0x980087da = null
            0x108153f2 = null
            0xeb569198 = null
            0xfccbb57e = null
            0x95984022 = null
            0xa18b224d = null
            0x02138de8 = null
            0xf8e85dd2 = null
            0x9abe70c9 = null
            0xa9151f50 = null
            0x5f9f527a = null
            0x463c9310 = null
            0x69b20303 = null
            0x47d0914a = null
            0x57137994 = null
            0x8ba9232a = null
            0x21769f7c = null
            0xd1203402 = null
            0xb772b261 = null
            0x57ad1b0a = null
            0x128eb2bc = null
            0xc559c272 = null
            0xf771ccf0 = null
            0xb1a558af = null
            0x77ec9c9b = null
            0x141b8e78 = null
            0xe108fb73 = null
            0x76d1c2e9 = null
            0x411eb286 = null
            0xb4d7c1cf = null
            0x203ed213 = null
            0x13a2c241 = null
            0x51973112 = null
            0x153f29e5 = null
            0xd8ac3b06 = null
            0xa4c30dcf = null
            0x46e3e4d1 = null
            0xeb7dc3a9 = null
            0x1da7ffda = null
            0x396a2c8a = null
            0xa4387b68 = null
            0xf4d8094d = null
            0xda52e34c = null
            0x4dcce093 = null
            0x298100d3 = null
            0xfe3849b0 = null
            0x8d3d42ee = null
            0x1aaa6864 = null
            0xecb6a892 = null
            0x479e5b44 = null
            0xd5533ce3 = null
            0x68ce268f = null
            0x87fd76fb = null
            0xd8938773 = null
            0x2537a0f7 = null
            0x24f106b4 = null
            0x1ab5f965 = null
            0x554fe300 = null
            0xd594ec52 = null
            0x3d5f8580 = null
            0x6773d33f = null
            0xc23d3c8a = null
            0xf0c9c374 = null
            0xedf58d54 = null
            0x6b398a6e = null
            0x6d2aa415 = null
            0xa33496aa = null
            0x9e93ab88 = null
            0xa2cd720e = null
            0x3aededd9 = null
            0x013f4a94 = null
            0x9c23ef06 = null
            0xa5a1bc93 = null
            0x82022c9e = null
            0x3e9d6a36 = null
            0x1f69cd65 = null
            0xdd6db1f0 = null
            0xd6fe9ebc = null
            0x8b5f9ea4 = null
            0x1f99bf95 = null
            0x3c296bdb = null
            0x757869a3 = null
            0x0d714bca = null
            0x5c732dbe = null
            0xf499897c = null
            0x0b3cfa20 = null
            0xf64e959c = null
            0x5eccea53 = null
            0xce4e4d47 = null
            0xbc4ad74f = null
            0xfd58f4d6 = null
            0x3b05bdb2 = null
            0x3a57b0c7 = null
            0x53c2f406 = null
            0xc2a7e1ee = null
            0x569a9db6 = null
            0x34e90f96 = null
            0xdfa2942c = null
            0xcd6b81a5 = null
            0x1a769626 = null
            0x70b43085 = null
            0x94d3a3fa = null
            0x2c81b1f1 = null
            0xc2b9dc2f = null
            0xf979b48c = null
            0xf5485cd2 = null
            0x01a533e2 = null
            0x02a649c8 = null
            0x3b3cf412 = null
            0x96de5bfa = null
            0x2397d999 = null
            0xb48ddc55 = null
            0x4d4d449e = null
            0x9ff3e666 = null
            0xa7427b95 = null
            0x77a8eb8d = null
            0xf9d47743 = null
            0x22474aa1 = null
            0x05e6b9ce = null
            0xde1db219 = null
            0xe263e61d = null
            0xf37459d1 = null
            0xd505f087 = null
            0x7876e5bc = null
            0x4690be48 = null
            0x131ea714 = null
            0x88a387e8 = null
            0x98a83053 = null
            0x431e3395 = null
            0x17fb1d85 = null
            0xde371c57 = null
            0x84c04798 = null
            0x16e33e90 = null
            0x0906f3fc = null
            0x57a1b16e = null
            0x6979c1ce = null
            0xb7e00c7c = null
            0x084bab28 = null
            0xfc8840da = null
            0xc2a16928 = null
            0x8e225b9a = null
            0x30c390d5 = null
            0x83ae1025 = null
            0xa3877a81 = null
            0x41b624ef = null
            0xeb7d7a3d = null
            0xae2c1a3d = null
            0x4103a853 = null
            0xaf7ed846 = null
            0xae7ef40b = null
            0x02896126 = null
            0x87780962 = null
            0x85102736 = null
            0x17674110 = null
            0x0546e77e = null
            0x81686705 = null
            0x4e727b05 = null
            0x13d03a81 = null
            0xec3ad324 = null
            0x20c6169b = null
            0x986d5d6b = null
            0xb179ce79 = null
            0x2ea50f41 = null
            0xfcf01cd3 = null
            0x94904eb2 = null
            0x521560e8 = null
            0x454bf22a = null
            0xbdc5ff6a = null
            0xf3f0ffda = null
            0xec3808ec = null
            0x702a291c = null
            0x5626206b = null
            0xcd00c1ad = null
            0x637b283c = null
            0x4808cf15 = null
            0xfa96f66a = null
            0x0fd9e0f4 = null
            0x5ffbaf14 = null
            0x75cb350e = null
            0x5ad6eac5 = null
            0xe8d6b3a3 = null
            0xf0aa51cf = null
            0x7780c4cb = null
            0xa1bafaf0 = null
            0x10e31c54 = null
            0xe1cede0f = null
            0x7ecaacb8 = null
            0x75edc05e = null
            0x4437a6e5 = null
            0xbe84ed84 = null
            0x40e9ba8c = null
            0x7352e08b = null
            0xac89f700 = null
            0x88c767d6 = null
            0x0f78166d = null
            0x0d84679b = null
            0x142a6692 = null
            0x27638f59 = null
            0xb01d1c93 = null
            0x582ac428 = null
            0xf64ecf1f = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7585.32129, -193.800064, 6798.5625, 1
                }
                name: string = "HA_AP_HealthRelic_Chaos_Outer"
            }
            0x04ebbc5d = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5929.7002, -194, 5190.8999, 1
                }
                name: string = "HA_AP_HealthRelic_Order_Outer"
            }
            0x6f87af9d = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8893.90039, -187.699997, 7889, 1
                }
                name: string = "HA_AP_HealthRelic_Chaos_Inner"
            }
            0x8f692346 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4790.2002, -188.5, 3934.30005, 1
                }
                name: string = "HA_AP_HealthRelic_Order_Inner"
            }
            0xa6c36cb6 = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 0.566658735
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3114.46313, -53.017334, 3979.98828, 1
                }
                name: string = "light_17_10"
            }
            0xb51aa881 = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 0.566658735
                intensityScale: f32 = 3.82222199
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2684.31055, 13.5881348, 3867.41479, 1
                }
                name: string = "light_17_11"
            }
            0x7fe7e51d = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 1.04431593
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5217.00537, 63.6325073, 5975.09766, 1
                }
                name: string = "light_17_12"
            }
            0x7f1104ea = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.18067658
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8891.82031, -57.1304626, 10556.7305, 1
                }
                name: string = "light_31_29"
            }
            0x220b8656 = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.18067658
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9523.21777, 12.9136353, 11175.6631, 1
                }
                name: string = "light_31_30"
            }
            0x87e4f7e2 = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.18067658
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10114.8633, 12.9137573, 11680.3711, 1
                }
                name: string = "light_31_31"
            }
            0xbf149072 = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 0.566658735
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3268.43994, -53.017334, 3996.25244, 1
                }
                name: string = "light_17_13"
            }
            0x33113df0 = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 0.789034784
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2107.38184, 13.5882568, 3867.33642, 1
                }
                name: string = "light_17_14"
            }
            0x2cc7b262 = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 0.789034784
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1879.30554, 13.5882568, 3836.98071, 1
                }
                name: string = "light_17_15"
            }
            0x2e74a2f4 = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 0.789034665
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1512.06067, 13.5883789, 3253.69141, 1
                }
                name: string = "light_17_16"
            }
            0x7b739cd1 = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 0.789034665
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    925.288574, 13.588501, 2722.91016, 1
                }
                name: string = "light_17_17"
            }
            0x8e1441a3 = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 0.789034665
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2485.81055, 13.5883789, 848.437988, 1
                }
                name: string = "light_17_18"
            }
            0x04b7f2c6 = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 0.789034665
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3414.67822, 13.5883789, 1731.91187, 1
                }
                name: string = "light_17_19"
            }
            0xddd607bc = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 0.789034665
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3204.18701, 13.5881348, 1429.59998, 1
                }
                name: string = "light_17_20"
            }
            0x9629fc77 = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 0.789034665
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1890.90112, 13.5878906, 180.152466, 1
                }
                name: string = "light_17_21"
            }
            0xa0040338 = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 0.566658735
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2935.27539, -53.017334, 3827.90478, 1
                }
                name: string = "light_17_22"
            }
            0xdfe35512 = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 0.566658735
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3738.71802, -53.0170898, 4631.08057, 1
                }
                name: string = "light_17_23"
            }
            0x22a38cec = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 0.566658735
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3944.08936, -53.017334, 4709.00928, 1
                }
                name: string = "light_17_24"
            }
            0xa1796fdc = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.18067658
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11163.9248, 12.9136353, 9174.79883, 1
                }
                name: string = "light_31_32"
            }
            0x0cfa82ef = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.18067658
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11280.1406, 12.9137573, 9433.87891, 1
                }
                name: string = "light_31_33"
            }
            0x67d604a8 = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.06360781
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11480.1416, 12.9133911, 9461.09863, 1
                }
                name: string = "light_31_34"
            }
            0x351ebb55 = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.06360781
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11904.1006, 12.9135132, 9810.41016, 1
                }
                name: string = "light_31_35"
            }
            0x8f882dca = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.06360781
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11954.0732, 12.9133911, 9967.13574, 1
                }
                name: string = "light_31_36"
            }
            0x6a9921c1 = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.06360781
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12039.8184, 12.9133911, 10045.1445, 1
                }
                name: string = "light_31_37"
            }
            0x3ba8d131 = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.18067658
                intensityScale: f32 = 3
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9345.66406, 12.9135742, 10954.9629, 1
                }
                name: string = "light_31_38"
            }
            0xbbb5e175 = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.18067658
                intensityScale: f32 = 3
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9511.50293, 12.913269, 10955.0644, 1
                }
                name: string = "light_31_39"
            }
            0x5387a574 = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.06990802
                intensityScale: f32 = 4
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9734.72852, 12.9137573, 11358.5342, 1
                }
                name: string = "light_31_40"
            }
            0x174a363d = MapPointLight {
                type: link = 0x613cd42e
                radiusScale: f32 = 1.18067658
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9042.25488, 12.9133911, 10610.3574, 1
                }
                name: string = "light_31_41"
            }
            0x311562d1 = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 0.566658735
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3762.69873, -53.0168457, 2860.73706, 1
                }
                name: string = "light_17_25"
            }
            0x6d811eec = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 0.566658735
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3884.84326, -53.0168457, 2630.4187, 1
                }
                name: string = "light_17_26"
            }
            0x45625eb4 = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 0.566658735
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3832.36401, -53.0167236, 3003.80493, 1
                }
                name: string = "light_17_27"
            }
            0x980c741b = MapPointLight {
                type: link = 0xd34204d2
                radiusScale: f32 = 0.627705634
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1260.9165, -10.5226746, 3143.12744, 1
                }
                name: string = "light_17_28"
            }
            0x5b73b4ee = MapPointLight {
                type: link = 0x684be9bd
                radiusScale: f32 = 0.556378484
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    845.207458, 6.40563965, 1664.73035, 1
                }
                name: string = "light_52_7"
            }
        }
        path: string = "Maps/MapGeometry/Map12/Chunks/Default"
    }
    "Maps/MapGeometry/Map12/Base" = mapContainer {
        mapPath: string = "Maps/MapGeometry/Map12/Base"
        components: list[pointer] = {
            MapSunProperties {
                sunColor: vec4 = { 0.36470589, 0.384313732, 0.392156869, 1 }
                sunDirection: vec3 = { -0.379999995, 0.707000017, 0.0500000007 }
                skyLightColor: vec4 = { 0.549019635, 0.580392182, 0.639215708, 1 }
                horizonColor: vec4 = { 0.631372571, 0.725490212, 0.815686285, 1 }
                groundColor: vec4 = { 0.274509817, 0.31764707, 0.41568628, 1 }
                skyLightScale: f32 = 0.800000012
                lightMapColorScale: f32 = 2
                fogColor: vec4 = { 0.211764708, 0.274509817, 0.407843143, 1 }
                fogAlternateColor: vec4 = { 0.20784314, 0.313725501, 0.498039216, 1 }
                fogStartAndEnd: vec2 = { -18361, -32711 }
            }
            MapBakeProperties {
                lightGridCharacterFullBrightIntensity: f32 = 0.5
                lightGridFileName: string = "ASSETS/Maps/Lightmaps/Maps/MapGeometry/Map12/Base/LightGrid.HA_Lighting_v2.dat"
            }
            MapLightingV2 {
                0xee91017d: f32 = 0.800000012
            }
        }
        boundsMin: vec2 = { -28.4299812, -19.0282936 }
        boundsMax: vec2 = { 12849.0957, 12858.4971 }
        lowestWalkableHeight: f32 = -220
        chunks: map[hash,link] = {
            "Default" = "Maps/MapGeometry/Map12/Chunks/Default"
        }
    }
    0x553a82b3 = MapPointLightType {
        lightColor: vec4 = { 0.192156881, 0.149019614, 0.600000024, 1 }
        radius: f32 = 963
        castStaticShadows: bool = false
    }
    0x584991f6 = MapPointLightType {
        lightColor: vec4 = { 0.00392156886, 0.34117648, 0.600000024, 1 }
        radius: f32 = 1184
        castStaticShadows: bool = false
    }
    0x593cc796 = MapPointLightType {
        lightColor: vec4 = { 0.623529434, 0.686274529, 0.721568644, 1 }
        radius: f32 = 497
        castStaticShadows: bool = false
    }
    0x59499389 = MapPointLightType {
        lightColor: vec4 = { 0.48627454, 0.48627454, 0.937254965, 1 }
        radius: f32 = 1761
        castStaticShadows: bool = false
    }
    0x5a3cc929 = MapPointLightType {
        lightColor: vec4 = { 0.796078503, 0.282352954, 0.92549026, 1 }
        radius: f32 = 497
    }
    0x5c3a8db8 = MapPointLightType {
        lightColor: vec4 = { 0.0274509825, 0.68235296, 0.929411829, 1 }
        radius: f32 = 852
        castStaticShadows: bool = false
    }
    0x5d3a8f4b = MapPointLightType {
        lightColor: vec4 = { 0.149019614, 0.458823532, 0.764705896, 1 }
        radius: f32 = 785
        castStaticShadows: bool = false
    }
    0x5d4bd86c = MapPointLightType {
        lightColor: vec4 = { 0.654901981, 0.760784388, 1, 1 }
        radius: f32 = 918
        castStaticShadows: bool = false
    }
    0x5e3a90de = MapPointLightType {
        lightColor: vec4 = { 0.56078434, 0.0470588282, 0.854902029, 1 }
        radius: f32 = 896
        castStaticShadows: bool = false
    }
    0x5e499b68 = MapPointLightType {
        lightColor: vec4 = { 0.207843155, 0.207843155, 0.215686291, 1 }
        radius: f32 = 1051
        castStaticShadows: bool = false
    }
    0x5e4bd9ff = MapPointLightType {
        lightColor: vec4 = { 0.749019623, 0.941176534, 1, 1 }
        radius: f32 = 652
        castStaticShadows: bool = false
    }
    0x5f3a9271 = MapPointLightType {
        lightColor: vec4 = { 0.513725519, 0.0627451017, 0.772549093, 1 }
        radius: f32 = 963
        castStaticShadows: bool = false
    }
    0x5f3cd108 = MapPointLightType {
        lightColor: vec4 = { 0.372549027, 0.392156869, 0.470588237, 1 }
        radius: f32 = 4000
        castStaticShadows: bool = false
    }
    0x5f499cfb = MapPointLightType {
        lightColor: vec4 = { 0.854902029, 0.854902029, 0.992156923, 1 }
        radius: f32 = 1140
        castStaticShadows: bool = false
    }
    0x603a9404 = MapPointLightType {
        lightColor: vec4 = { 0.0313725509, 0.301960796, 0.607843161, 1 }
        radius: f32 = 1184
    }
    0x603cd29b = MapPointLightType {
        lightColor: vec4 = { 0.0941176489, 0.686274529, 0.400000006, 1 }
        radius: f32 = 519
    }
    0x613a9597 = MapPointLightType {
        lightColor: vec4 = { 0.360784322, 0.525490224, 0.831372619, 1 }
        radius: f32 = 1739
        castStaticShadows: bool = false
    }
    0x613cd42e = MapPointLightType {
        lightColor: vec4 = { 0.635294139, 0.137254909, 0.0352941193, 1 }
        radius: f32 = 253
        castStaticShadows: bool = false
    }
    0x6149a021 = MapPointLightType {
        lightColor: vec4 = { 0.984313786, 0.80392164, 0.996078491, 1 }
        radius: f32 = 852
        castStaticShadows: bool = false
    }
    0x614bdeb8 = MapPointLightType {
        lightColor: vec4 = { 0.0313725509, 0.0313725509, 0.0352941193, 1 }
        radius: f32 = 941
    }
    0x623a972a = MapPointLightType {
        lightColor: vec4 = { 0.694117665, 0.215686291, 0.870588303, 1 }
        radius: f32 = 1074
        castStaticShadows: bool = false
    }
    0x623cd5c1 = MapPointLightType {
        lightColor: vec4 = { 0.941176534, 0.215686291, 0.0509803966, 1 }
        radius: f32 = 431
        castStaticShadows: bool = false
    }
    0x6249a1b4 = MapPointLightType {
        lightColor: vec4 = { 0.309803933, 0.356862754, 0.403921574, 1 }
        radius: f32 = 1872
        castStaticShadows: bool = false
    }
    0x624be04b = MapPointLightType {
        lightColor: vec4 = { 0.811764717, 0.933333337, 0.941176474, 1 }
        radius: f32 = 542
        castStaticShadows: bool = false
    }
    0x633a98bd = MapPointLightType {
        lightColor: vec4 = { 0.113725491, 0.470588237, 0.709803939, 1 }
        radius: f32 = 918
    }
    0x633cd754 = MapPointLightType {
        lightColor: vec4 = { 0.980392218, 0.53725493, 0.501960814, 1 }
        radius: f32 = 475
        castStaticShadows: bool = false
    }
    0x6349a347 = MapPointLightType {
        lightColor: vec4 = { 0.301960796, 0.607843161, 0.694117665, 1 }
        radius: f32 = 1051
        castStaticShadows: bool = false
    }
    0x634be1de = MapPointLightType {
        lightColor: vec4 = { 1, 0.450980425, 0.423529446, 1 }
        radius: f32 = 630
        castStaticShadows: bool = false
    }
    0x643cd8e7 = MapPointLightType {
        lightColor: vec4 = { 0.988235354, 0.494117677, 0.00784313772, 1 }
        radius: f32 = 342
        castStaticShadows: bool = false
    }
    0x6449a4da = MapPointLightType {
        lightColor: vec4 = { 0.298039228, 0.298039228, 0.388235301, 1 }
        radius: f32 = 1650
        castStaticShadows: bool = false
    }
    0x644be371 = MapPointLightType {
        lightColor: vec4 = { 0.996078491, 0.482352972, 0.227450997, 1 }
        radius: f32 = 586
        castStaticShadows: bool = false
    }
    0x6549a66d = MapPointLightType {
        lightColor: vec4 = { 0.235294119, 0.258823544, 0.278431386, 1 }
        radius: f32 = 3490
        castStaticShadows: bool = false
    }
    0x654be504 = MapPointLightType {
        lightColor: vec4 = { 0.427451015, 0.600000024, 0.839215755, 1 }
        radius: f32 = 652
        castStaticShadows: bool = false
    }
    0x664be697 = MapPointLightType {
        lightColor: vec4 = { 0.141176477, 0.294117659, 0.313725501, 1 }
        radius: f32 = 1982
        castStaticShadows: bool = false
    }
    0x674be82a = MapPointLightType {
        lightColor: vec4 = { 0.501960814, 0.796078503, 0.952941239, 1 }
        radius: f32 = 1207
        castStaticShadows: bool = false
    }
    0x684be9bd = MapPointLightType {
        lightColor: vec4 = { 0.819607854, 0.925490201, 0.949019611, 1 }
        radius: f32 = 564
        castStaticShadows: bool = false
    }
    0xcd41fb60 = MapPointLightType {
        lightColor: vec4 = { 0.878431439, 0.262745112, 0.0509803966, 1 }
        radius: f32 = 564
        castStaticShadows: bool = false
    }
    0xce41fcf3 = MapPointLightType {
        lightColor: vec4 = { 0.0313725509, 0.0823529437, 0.172549024, 1 }
        radius: f32 = 719
        castStaticShadows: bool = false
    }
    0xcf41fe86 = MapPointLightType {
        lightColor: vec4 = { 0.458823562, 0.054901965, 0.878431439, 1 }
        radius: f32 = 630
        castStaticShadows: bool = false
    }
    0xd0420019 = MapPointLightType {
        lightColor: vec4 = { 0.56078434, 0.0392156877, 0.92549026, 1 }
        radius: f32 = 741
        castStaticShadows: bool = false
    }
    0xd14201ac = MapPointLightType {
        lightColor: vec4 = { 0.0274509825, 0.36470589, 0.870588303, 1 }
        radius: f32 = 1096
        castStaticShadows: bool = false
    }
    0xd242033f = MapPointLightType {
        lightColor: vec4 = { 0.490196109, 0.784313798, 0.992156923, 1 }
        radius: f32 = 675
        castStaticShadows: bool = false
    }
    0xd338a4e6 = MapPointLightType {
        lightColor: vec4 = { 0.678431392, 0.0352941193, 0.709803939, 1 }
        radius: f32 = 1051
    }
    0xd34204d2 = MapPointLightType {
        lightColor: vec4 = { 0.796078503, 0.239215702, 0.0666666701, 1 }
        radius: f32 = 519
        castStaticShadows: bool = false
    }
    0xd438a679 = MapPointLightType {
        lightColor: vec4 = { 0.0156862754, 0.68235296, 0.960784376, 1 }
        radius: f32 = 1051
        castStaticShadows: bool = false
    }
    0xd4420665 = MapPointLightType {
        lightColor: vec4 = { 0.952941239, 0.360784322, 0.0980392247, 1 }
        radius: f32 = 276
    }
    0xd44444fc = MapPointLightType {
        lightColor: vec4 = { 0.988235354, 0.423529446, 0.00784313772, 1 }
        radius: f32 = 719
        castStaticShadows: bool = false
    }
    0xd544468f = MapPointLightType {
        lightColor: vec4 = { 0.890196145, 0.670588255, 0.94901967, 1 }
        radius: f32 = 519
        castStaticShadows: bool = false
    }
    0xd642098b = MapPointLightType {
        lightColor: vec4 = { 0.337254912, 0.56078434, 0.53725493, 1 }
        radius: f32 = 2160
    }
    0xd6444822 = MapPointLightType {
        lightColor: vec4 = { 0.980392218, 0.223529428, 0.403921604, 1 }
        radius: f32 = 475
        castStaticShadows: bool = false
    }
    0xdd38b4a4 = MapPointLightType {
        lightColor: vec4 = { 0.850980461, 0.176470593, 0, 1 }
        radius: f32 = 564
        castStaticShadows: bool = false
    }
    0xde38b637 = MapPointLightType {
        lightColor: vec4 = { 0.0392156877, 0.792156935, 0.882353008, 1 }
        radius: f32 = 608
    }
}
