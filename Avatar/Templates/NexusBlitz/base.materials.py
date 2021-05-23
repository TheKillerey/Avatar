#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Maps/KitPieces/Prototype/Materials/_chunk_jungle_south_island_i_Alpha_3dcUV_Atlas_color_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/_chunk_jungle_south_island_i_Alpha_3dcUV_Atlas_color_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/_chunk_jungle_south_island_i_Alpha_3dcUV_Atlas_color.dds"
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
    "Maps/KitPieces/Prototype/Materials/_chunk_jungle_south_island_h_Alpha_3dcUV_Atlas_color_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/_chunk_jungle_south_island_h_Alpha_3dcUV_Atlas_color_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/_chunk_jungle_south_island_h_Alpha_3dcUV_Atlas_color.dds"
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
    "Maps/KitPieces/Prototype/Materials/_chunk_jungle_north_island_b_Alpha_3dcUV_Atlas_color_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/_chunk_jungle_north_island_b_Alpha_3dcUV_Atlas_color_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/_chunk_jungle_north_island_b_Alpha_3dcUV_Atlas_color.dds"
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
    "Maps/KitPieces/Prototype/Materials/ds_rock_filler_a_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/ds_rock_filler_a_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/ds_rock_filler_a.dds"
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
    "Maps/KitPieces/Prototype/Materials/periph_south_g_combined2_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/periph_south_g_combined2_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/periph_south_g_combined2.dds"
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
    "Maps/KitPieces/Prototype/Materials/_chunk_jungle_north_island_a_Alpha_3dcUV_Atlas_color_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/_chunk_jungle_north_island_a_Alpha_3dcUV_Atlas_color_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/_chunk_jungle_north_island_a_Alpha_3dcUV_Atlas_color.dds"
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
    "Maps/KitPieces/Prototype/Materials/wooden_torch_TX_DM2_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/wooden_torch_TX_DM2_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/nb_wooden_torch_a.dds"
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
    "Maps/KitPieces/Prototype/Materials/periph_north_j11_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/periph_north_j11_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/Periph_north_J1.dds"
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
    "Maps/KitPieces/Prototype/Materials/ds_sideplatform_diff_01_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/ds_sideplatform_diff_01_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/ds_SidePlatform_diff_01.dds"
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
    "Maps/KitPieces/Prototype/Materials/_chunk_jungle_west_island_g_Alpha_3dcUV_Atlas_color_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/_chunk_jungle_west_island_g_Alpha_3dcUV_Atlas_color_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/_chunk_jungle_west_island_g_Alpha_3dcUV_Atlas_color.dds"
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
    "Maps/KitPieces/Prototype/Materials/_chunk_jungle_south_island_d_Alpha_3dcUV_Atlas_color_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/_chunk_jungle_south_island_d_Alpha_3dcUV_Atlas_color_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/_chunk_jungle_south_island_d_Alpha_3dcUV_Atlas_color.dds"
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
    "Maps/KitPieces/Prototype/Materials/periph_north_l_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/periph_north_l_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/periph_north_l.dds"
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
    "Maps/KitPieces/Prototype/Materials/wolf_mat_alpha_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/wolf_mat_alpha_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/wolf_card.dds"
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
    "Maps/KitPieces/Prototype/Materials/midlane_platform_top_a_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/midlane_platform_top_a_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/NPE_midlane_platform_top_a.dds"
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
    "Maps/KitPieces/Prototype/Materials/jungle_west_island_a1_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/jungle_west_island_a1_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/jungle_west_island_a.dds"
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
    "Maps/KitPieces/Prototype/Materials/lambert172811_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/lambert172811_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/shop_props.dds"
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
    "Maps/KitPieces/Prototype/Materials/Periph_Southeast_A1_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/Periph_Southeast_A1_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/Periph_Southeast_A1.dds"
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
    "Maps/KitPieces/Prototype/Materials/SG_rocks_b_alpha_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/SG_rocks_b_alpha_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/SG_rocks_b.dds"
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
    "Maps/KitPieces/Prototype/Materials/_chunk_jungle_south_island_e_Alpha_3dcUV_Atlas_color_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/_chunk_jungle_south_island_e_Alpha_3dcUV_Atlas_color_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/_chunk_jungle_south_island_e_Alpha_3dcUV_Atlas_color.dds"
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
    "Maps/KitPieces/Prototype/Materials/tower_scorch_mat_alpha_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/tower_scorch_mat_alpha_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/tower_scorch.dds"
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
    "Maps/KitPieces/Prototype/Materials/nb_crashsite_decal_a_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/nb_crashsite_decal_a_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/nb_crashsite_decal_a.dds"
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
    "Maps/KitPieces/Prototype/Materials/NB_Rubble_A_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/NB_Rubble_A_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/NB_Rubble_A.dds"
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
    "Maps/KitPieces/Prototype/Materials/periph_west_a4_alpha_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/periph_west_a4_alpha_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/periph_west_a4.dds"
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
    "Maps/KitPieces/Prototype/Materials/_chunk_jungle_west_island_e_Alpha_3dcUV_Atlas_color_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/_chunk_jungle_west_island_e_Alpha_3dcUV_Atlas_color_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/_chunk_jungle_west_island_e_Alpha_3dcUV_Atlas_color.dds"
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
    "Maps/KitPieces/Prototype/Materials/ds_SpawnPlat_diff_01_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/ds_SpawnPlat_diff_01_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/ds_SpawnPlat_diff_01.dds"
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
    "Maps/KitPieces/Prototype/Materials/periph_west_c4_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/periph_west_c4_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/periph_west_c4.dds"
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
    "Maps/KitPieces/Prototype/Materials/Periph_East_A1_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/Periph_East_A1_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/Periph_East_A1.dds"
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
    "Maps/KitPieces/Prototype/Materials/_chunk_jungle_west_island_d_Alpha_3dcUV_Atlas_color_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/_chunk_jungle_west_island_d_Alpha_3dcUV_Atlas_color_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/_chunk_jungle_west_island_d_Alpha_3dcUV_Atlas_color.dds"
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
    "Maps/KitPieces/Prototype/Materials/krug_mat_alpha_blend_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/krug_mat_alpha_blend_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/krug_ground.dds"
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
    "Maps/KitPieces/Prototype/Materials/_chunk_jungle_north_island_g_Alpha_3dcUV_Atlas_color_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/_chunk_jungle_north_island_g_Alpha_3dcUV_Atlas_color_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/_chunk_jungle_north_island_g_Alpha_3dcUV_Atlas_color.dds"
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
    "Maps/KitPieces/Prototype/Materials/_chunk_jungle_west_island_i_Alpha_3dcUV_Atlas_color_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/_chunk_jungle_west_island_i_Alpha_3dcUV_Atlas_color_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/_chunk_jungle_west_island_i_Alpha_3dcUV_Atlas_color.dds"
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
    "Maps/KitPieces/Prototype/Materials/_chunk_jungle_south_island_k_alpha_3dcuv_atlas_color_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/_chunk_jungle_south_island_k_alpha_3dcuv_atlas_color_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/_chunk_jungle_south_island_k_Alpha_3dcUV_Atlas_color.dds"
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
    "Maps/KitPieces/Prototype/Materials/NPE_midlane_platform_top_b_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/NPE_midlane_platform_top_b_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/NPE_midlane_platform_top_b.dds"
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
    "Maps/KitPieces/Prototype/Materials/Periph_Southeast_C3_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/Periph_Southeast_C3_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/Periph_Southeast_C3.dds"
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
    "Maps/KitPieces/Prototype/Materials/periph_base_south_west_a_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/periph_base_south_west_a_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/periph_base_south_west_a.dds"
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
    "Maps/KitPieces/Prototype/Materials/SG_periph_rocks_a_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/SG_periph_rocks_a_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/SG_periph_rocks_a.dds"
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
    "Maps/KitPieces/Prototype/Materials/Periph_South_F1a_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/Periph_South_F1a_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/Periph_South_F1a.dds"
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
    "Maps/KitPieces/Prototype/Materials/nest_mat_alpha_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/nest_mat_alpha_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/Camp_Nest.dds"
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
    "Maps/KitPieces/Prototype/Materials/sru_tower_decal_01_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/sru_tower_decal_01_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/sru_tower_decal_01.dds"
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
    "Maps/KitPieces/Prototype/Materials/base_north_arches_periph6_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/base_north_arches_periph6_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/base_north_arches_periph.dds"
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
    "Maps/KitPieces/Prototype/Materials/_chunk_jungle_north_island_d_Alpha_3dcUV_Atlas_color_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Prototype/Materials/_chunk_jungle_north_island_d_Alpha_3dcUV_Atlas_color_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Prototype/textures/_chunk_jungle_north_island_d_Alpha_3dcUV_Atlas_color.dds"
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
    "Maps/KitPieces/Snowdown/Materials/Snow_Tree_Ornaments_A_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Snowdown/Materials/Snow_Tree_Ornaments_A_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Snowdown/textures/Snow_Tree_Ornaments_A.dds"
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
    "Maps/KitPieces/Snowdown/Materials/Snow_Lights_A_Diff_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Snowdown/Materials/Snow_Lights_A_Diff_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Snowdown/textures/Snow_Lights_A_Diff.dds"
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
    "Maps/KitPieces/Snowdown/Materials/Snow_Gifts_A_Diff_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Snowdown/Materials/Snow_Gifts_A_Diff_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Snowdown/textures/Snow_Gifts_A_Diff.dds"
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
    "Maps/KitPieces/Snowdown/Materials/Snow_Teddy_A_diff_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Snowdown/Materials/Snow_Teddy_A_diff_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Snowdown/textures/Snow_Teddy_A_diff.dds"
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
    "Maps/KitPieces/Snowdown/Materials/Snow_Gingerbread_A_diff_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Snowdown/Materials/Snow_Gingerbread_A_diff_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Snowdown/textures/Snow_Gingerbread_A_diff.dds"
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
    "Maps/KitPieces/Snowdown/Materials/sd_sled_01_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Snowdown/Materials/sd_sled_01_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Snowdown/textures/sd_sled_01.dds"
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
    "Maps/KitPieces/Snowdown/Materials/Snow_Barrel_A_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Snowdown/Materials/Snow_Barrel_A_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Snowdown/textures/Snow_Barrel_A.dds"
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
    "Maps/KitPieces/Snowdown/Materials/lambert4_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Snowdown/Materials/lambert4_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Snowdown/textures/Snow_Lights_A_Diff.dds"
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
    "Maps/Particles/SR/SRU_Chaos_BaseDoor_GlowChild" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                emitterName: string = "GlowChild"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_chaos_basedoor_glowchild.scb"
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
                pass: i16 = 5
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                texture: string = "ASSETS/Shared/Particles/SRU_Chaos_BaseDoor_Glow.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.300000012, -0.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                            { 0.300000012, -0.5 }
                        }
                    }
                }
            }
        }
        particleName: string = "SRU_Chaos_BaseDoor_GlowChild"
        particlePath: string = "Maps/Particles/SR/SRU_Chaos_BaseDoor_GlowChild"
        assetRemappingTable: list[embed] = {
            VfxAssetRemap {
                oldAsset: hash = 0x8ced37d7
                newAsset: string = "ASSETS/Shared/Particles/SRU_Order_BaseDoor_Glow.dds"
            }
        }
    }
    "Maps/Particles/SR/Sru_braziers_fire" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
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
                                    0.800000012
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
                    constantValue: vec3 = { 0, 300, 0 }
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
                            { 0, 300, 0 }
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
                pass: i16 = 2
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
                                    0
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
                    constantValue: vec3 = { 35, 35, 35 }
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
                            { 35, 35, 35 }
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
                texture: string = "ASSETS/Maps/Particles/SR/SRU_Brazier_Flame_Temp_01.DDS"
                numFrames: u16 = 8
                texDiv: vec2 = { 4, 2 }
                textureMult: string = "ASSETS/Maps/Particles/SR/Env_MB_brazierFire_mult.dds"
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
                    constantValue: f32 = 3
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
                                    0.5
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
                emitterName: string = "baseGlow"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -1, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 0.5, 0.5, 0.5 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 80, 80 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.75, 0.75, 0.75 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/SR/SRU_brazierFire_glow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
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
                            1.20000005
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11.1999998
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
                    constantValue: vec3 = { 0, 250, 0 }
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
                            { 0, 250, 0 }
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
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
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
                            { 20, 20, 0 }
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
                texture: string = "ASSETS/Maps/Particles/SR/Env_MB_brazierFire_Ash_01.dds"
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
                    constantValue: vec3 = { 0, 150, 0 }
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
                            { 0, 150, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 30, 20, 10 }
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
                                { 30, 20, 10 }
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
                            { 1, 1, 0.227450997, 0 }
                            { 0.901961029, 0.890196025, 0.713724971, 0.298038989 }
                            { 0.74901998, 0.745097995, 0.55686301, 0.0980390012 }
                            { 0.290196002, 0.478430986, 1, 0 }
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
                    constantValue: vec3 = { 70, 70, 0 }
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
                            { 70, 70, 0 }
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
                texture: string = "ASSETS/Maps/Particles/SR/Env_MB_brazier_dust.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.400000006 }
                }
                textureMult: string = "ASSETS/Maps/Particles/SR/Env_MB_brazier_dust_mult.dds"
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
                    constantValue: f32 = 0.0799999982
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 22
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
                            22
                        }
                    }
                }
                particleLinger: option[f32] = {
                    32
                }
                emitterName: string = "FireGlow"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 0 }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.349999994
                            0.449999988
                            0.550000012
                            0.649999976
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.550000012 }
                            { 1, 1, 1, 0.850000024 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.850000024 }
                            { 1, 1, 1, 0.550000012 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
                miscRenderFlags: u8 = 1
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 151, 151, 151 }
                }
                texture: string = "ASSETS/Maps/Particles/SR/SRU_Brazier_Glow_01.dds"
            }
        }
        particleName: string = "Sru_braziers_fire"
        particlePath: string = "Maps/Particles/SR/Sru_braziers_fire"
        soundPersistentDefault: string = "Play_sfx_Env_Map11_Emitter_firebig"
    }
    "Maps/Particles/SR/Sru_torch_fire" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
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
                                    0.800000012
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
                    constantValue: vec3 = { 0, 300, 0 }
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
                            { 0, 300, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 10, 10, 10 }
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
                                { 10, 10, 10 }
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
                pass: i16 = 2
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
                                    0
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
                    constantValue: vec3 = { 35, 35, 35 }
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
                            { 35, 35, 35 }
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
                texture: string = "ASSETS/Maps/Particles/SR/SRU_Brazier_Flame_Temp_01.DDS"
                numFrames: u16 = 8
                texDiv: vec2 = { 4, 2 }
                textureMult: string = "ASSETS/Maps/Particles/SR/Env_MB_brazierFire_mult.dds"
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
                    constantValue: f32 = 3
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
                                    0.5
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
                emitterName: string = "baseGlow"
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
                            { 1, 0.5, 0.5, 0.5 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 80, 80 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.75, 0.75, 0.75 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/SR/SRU_brazierFire_glow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
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
                            1.20000005
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11.1999998
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
                    constantValue: vec3 = { 0, 250, 0 }
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
                            { 0, 250, 0 }
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
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
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
                            { 20, 20, 0 }
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
                texture: string = "ASSETS/Maps/Particles/SR/Env_MB_brazierFire_Ash_01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
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
                    constantValue: vec3 = { 0, 150, 0 }
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
                            { 0, 150, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 15, 20, 5 }
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
                                { 15, 20, 5 }
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
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.62999922 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 0.227450997, 0 }
                            { 0.901961029, 0.890196025, 0.713724971, 0.178823397 }
                            { 0.74901998, 0.745097995, 0.55686301, 0.0588233992 }
                            { 0.290196002, 0.478430986, 1, 0 }
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
                    constantValue: vec3 = { 70, 70, 0 }
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
                            { 70, 70, 0 }
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
                texture: string = "ASSETS/Maps/Particles/SR/Env_MB_brazier_dust.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.400000006 }
                }
                textureMult: string = "ASSETS/Maps/Particles/SR/Env_MB_brazier_dust_mult.dds"
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
                    constantValue: f32 = 0.0799999982
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 22
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
                            22
                        }
                    }
                }
                particleLinger: option[f32] = {
                    32
                }
                emitterName: string = "FireGlow"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 0 }
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
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.349999994
                            0.449999988
                            0.550000012
                            0.649999976
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.550000012 }
                            { 1, 1, 1, 0.850000024 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.850000024 }
                            { 1, 1, 1, 0.550000012 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
                miscRenderFlags: u8 = 1
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 85, 85, 85 }
                }
                texture: string = "ASSETS/Maps/Particles/SR/SRU_Brazier_Glow_01.dds"
            }
        }
        particleName: string = "Sru_torch_fire"
        particlePath: string = "Maps/Particles/SR/Sru_torch_fire"
        soundPersistentDefault: string = "Play_sfx_Env_Map11_Emitter_firebig"
    }
    "Maps/Particles/SR/SLIME_turret_AOE" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    100000
                }
                emitterName: string = "Temp_Mesh"
                disabled: bool = true
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -10, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/SLIME/SLIME_Fountain_Danger_AOE_Mesh.scb"
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
                            { 1, 0.725490212, 0.529411793, 1 }
                            { 0.0588235296, 1, 0.0117647061, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0.5
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/Maps/Particles/SLIME/SLIME_Flame_Circle.dds"
                }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3.70000005, 3.79999995, 4 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.574999988, 0.574999988, 0.574999988 }
                }
                texture: string = "ASSETS/Maps/Particles/SLIME/SLIME_Flame_Turret_Circle.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
                texDiv: vec2 = { 0.5, 1 }
                textureMult: string = "ASSETS/Maps/Particles/SLIME/SLIME_Danger_AOE_Dome_Fire_Mult.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    100000
                }
                emitterName: string = "Temp_Mesh2"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -10, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/SLIME/SLIME_Fountain_Danger_AOE_Mesh.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.229999244, 0.229999244, 0.229999244, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.229999244, 0.229999244, 0.229999244, 0 }
                            { 0.229999244, 0.16686219, 0.121764302, 0.500007629 }
                            { 0.229999244, 0, 0, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/Maps/Particles/SLIME/SLIME_Flame_Circle.dds"
                }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3.70000005, 4, 4 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.574999988, 1, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/SLIME/SLIME_Flame_Turret_Circle.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
                texDiv: vec2 = { 0.5, 1 }
                textureMult: string = "ASSETS/Maps/Particles/SLIME/SLIME_Danger_AOE_Dome_Fire_Mult.dds"
            }
        }
        visibilityRadius: f32 = 10000
        particleName: string = "SLIME_turret_AOE"
        particlePath: string = "Maps/Particles/SR/SLIME_turret_AOE"
        flags: u8 = 197
    }
    "Maps/Particles/SR/SRU_Chaos_BaseDoor_Glow" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                emitterName: string = "Glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_chaos_basedoor_glow.scb"
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
                pass: i16 = 5
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                texture: string = "ASSETS/Shared/Particles/SRU_Chaos_BaseDoor_Glow.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.300000012, -0.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                            { 0.300000012, -0.5 }
                        }
                    }
                }
            }
        }
        particleName: string = "SRU_Chaos_BaseDoor_Glow"
        particlePath: string = "Maps/Particles/SR/SRU_Chaos_BaseDoor_Glow"
        assetRemappingTable: list[embed] = {
            VfxAssetRemap {
                oldAsset: hash = 0x8ced37d7
                newAsset: string = "ASSETS/Shared/Particles/SRU_Order_BaseDoor_Glow.dds"
            }
        }
    }
    "Maps/Particles/SR/SRU_Order_BaseDoor_Glow" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                emitterName: string = "Glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_order_basedoor_glow.scb"
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
                pass: i16 = 5
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                texture: string = "ASSETS/Shared/Particles/SRU_Order_BaseDoor_Glow.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.300000012, -0.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                            { 0.300000012, -0.5 }
                        }
                    }
                }
            }
        }
        particleName: string = "SRU_Order_BaseDoor_Glow"
        particlePath: string = "Maps/Particles/SR/SRU_Order_BaseDoor_Glow"
        assetRemappingTable: list[embed] = {
            VfxAssetRemap {
                oldAsset: hash = 0x64f7a797
                newAsset: string = "ASSETS/Shared/Particles/SRU_Chaos_BaseDoor_Glow.dds"
            }
        }
    }
    "Maps/Particles/SR/SRU_Order_BaseDoor_GlowChild" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                emitterName: string = "GlowChild"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_order_basedoor_glowchild.scb"
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
                pass: i16 = 5
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                texture: string = "ASSETS/Shared/Particles/SRU_Order_BaseDoor_Glow.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.300000012, -0.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                            { 0.300000012, -0.5 }
                        }
                    }
                }
            }
        }
        particleName: string = "SRU_Order_BaseDoor_GlowChild"
        particlePath: string = "Maps/Particles/SR/SRU_Order_BaseDoor_GlowChild"
        assetRemappingTable: list[embed] = {
            VfxAssetRemap {
                oldAsset: hash = 0x64f7a797
                newAsset: string = "ASSETS/Shared/Particles/SRU_Chaos_BaseDoor_Glow.dds"
            }
        }
    }
    "Maps/Particles/Odyssey/Odyssey_wispfly" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5.5
                }
                particleLinger: option[f32] = {
                    15.5
                }
                emitterName: string = "wispFly"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1400, 0, 0 }
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
                                { 1400, 0, 0 }
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/Odyssey/sru_sjungle_wispfly.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.355993003 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.355993003 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -45.2000008, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1.5, 1.5 }
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
                                    0.699999988
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1.5, 1.5, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/Odyssey/SRU_SJungle_wispFly.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.150000006, 0 }
                }
            }
        }
        particleName: string = "Odyssey_wispfly"
        particlePath: string = "Maps/Particles/Odyssey/Odyssey_wispfly"
    }
    "Maps/Particles/Odyssey/Odyssey_Godrays" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLinger: option[f32] = {
                    20
                }
                emitterName: string = "Godray"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 600, 1, 600 }
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
                                { 600, 1, 600 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/Odyssey/sru_njungle_godray.scb"
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
                pass: i16 = 100
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Maps/Particles/Odyssey/SRU_NJungle_GodRays.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.25, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0.0500000007
                                    0.0500000007
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.25, 0 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
        }
        visibilityRadius: f32 = 400
        particleName: string = "Odyssey_Godrays"
        particlePath: string = "Maps/Particles/Odyssey/Odyssey_Godrays"
        flags: u8 = 132
    }
    "Maps/Particles/Odyssey/Odyssey_Motes_Ground" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.39999998
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.39999998
                        }
                    }
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
                                    0.5
                                    3
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
                    12
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldOrbitalDefinitions: list[embed] = {
                        VfxFieldOrbitalDefinitionData {
                            isLocalSpace: bool = false
                        }
                    }
                }
                emitterName: string = "sparkleorbs"
                disabled: bool = true
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 120, 90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    -1
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
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 120, 90 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.300000012, 0 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 30, 1, 30 }
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
                                { 30, 1, 30 }
                            }
                        }
                    }
                }
                particleColorTexture: string = "ASSETS/Shared/Particles/color-bellcurve4.DDS"
                pass: i16 = 50
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/Odyssey/SRU_Bluebuff_sparkleorbs.dds"
                numFrames: u16 = 8
                startFrame: u16 = 1
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.300000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            10
                        }
                    }
                }
                particleLinger: option[f32] = {
                    20
                }
                emitterName: string = "Motes"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 2, 3 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.400000006
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -3
                                    1
                                    3
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.400000006
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -3
                                    1
                                    3
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 3, 2, 3 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 400, 400, 400 }
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
                                { 400, 400, 400 }
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
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.400000006 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.400000006 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
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
                            { 1, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 4, 4, 4 }
                            { 20, 20, 20 }
                            { 4, 4, 4 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/Odyssey/SRU_Lane_motes.dds"
                numFrames: u16 = 2
                texDiv: vec2 = { 1, 2 }
            }
        }
        particleName: string = "Odyssey_Motes_Ground"
        particlePath: string = "Maps/Particles/Odyssey/Odyssey_Motes_Ground"
    }
    "Maps/Particles/Odyssey/Odyssey_Ground_Wind" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.400000006
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.899999976
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
                emitterName: string = "WindGrass1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 0, 0 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 60, 0, 130 }
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
                                { 60, 0, 130 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = -40
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
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/Odyssey/SRU_wolfden_blueside_windgrass_01.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.800000012 }
                            { 1, 1, 1, 0.800000012 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -10, 0 }
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
                            { 0, -10, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
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
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/Odyssey/SRU_WolfDen_Blueside_WindGrass_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.800000012, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.899999976
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.800000012, 0 }
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
                                    0.5
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
                textureMult: string = "ASSETS/Maps/Particles/Odyssey/SRU_WolfDen_Blueside_WindGrass_Mult_01.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                }
            }
        }
        particleName: string = "Odyssey_Ground_Wind"
        particlePath: string = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
    }
    "Maps/Particles/Snowdown/SRU_Snowdown_TreeLights_02" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
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
                                    1
                                    2
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
                    18
                }
                emitterName: string = "Basic"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emissionMeshName: string = "ASSETS/Maps/Particles/Snowdown/SRU_TreeLights_Emitter_02.scb"
                particleColorTexture: string = "ASSETS/Maps/Particles/Snowdown/color-bellcurve4.DDS"
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
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -90
                                    90
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
                    constantValue: vec3 = { 6, 3, 3 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    3
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 6, 3, 3 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/Snowdown/SRU_Snowdown_TreeLights.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    15
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
                                constantValue: f32 = 25
                            }
                            axisFraction: vec3 = { 1, 1, 0.5 }
                        }
                    }
                }
                emitterName: string = "Firefly"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
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
                            { 5, 5, 5 }
                        }
                    }
                }
                emissionMeshName: string = "ASSETS/Maps/Particles/Snowdown/SRU_TreeLights_Emitter_02.scb"
                particleColorTexture: string = "ASSETS/Maps/Particles/Snowdown/color-bellcurve4.DDS"
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
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -90
                                    90
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
                    constantValue: vec3 = { 6, 3, 3 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    3
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 6, 3, 3 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/Snowdown/SRU_Snowdown_TreeLights.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/Snowdown/SRU_TreeLights_Emitter_02.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.400000006 }
                }
                texture: string = "ASSETS/Shared/Particles/checkers.dds"
            }
        }
        visibilityRadius: f32 = 1500
        particleName: string = "SRU_Snowdown_TreeLights_02"
        particlePath: string = "Maps/Particles/Snowdown/SRU_Snowdown_TreeLights_02"
        flags: u8 = 132
    }
    "Maps/Particles/Snowdown/SRU_Snowdown_TreeLights_01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
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
                                    1
                                    2
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
                    18
                }
                emitterName: string = "Basic"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emissionMeshName: string = "ASSETS/Maps/Particles/Snowdown/SRU_TreeLights_Emitter_01.scb"
                particleColorTexture: string = "ASSETS/Maps/Particles/Snowdown/color-bellcurve4.DDS"
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
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -90
                                    90
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
                    constantValue: vec3 = { 6, 3, 3 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    3
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 6, 3, 3 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/Snowdown/SRU_Snowdown_TreeLights.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    15
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
                                constantValue: f32 = 25
                            }
                            axisFraction: vec3 = { 1, 1, 0.5 }
                        }
                    }
                }
                emitterName: string = "Firefly"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
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
                            { 5, 5, 5 }
                        }
                    }
                }
                emissionMeshName: string = "ASSETS/Maps/Particles/Snowdown/SRU_TreeLights_Emitter_01.scb"
                particleColorTexture: string = "ASSETS/Maps/Particles/Snowdown/color-bellcurve4.DDS"
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
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -90
                                    90
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
                    constantValue: vec3 = { 6, 3, 3 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    3
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 6, 3, 3 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/Snowdown/SRU_Snowdown_TreeLights.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/Snowdown/SRU_TreeLights_Emitter_01.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.400000006 }
                }
                texture: string = "ASSETS/Shared/Particles/checkers.dds"
            }
        }
        visibilityRadius: f32 = 1500
        particleName: string = "SRU_Snowdown_TreeLights_01"
        particlePath: string = "Maps/Particles/Snowdown/SRU_Snowdown_TreeLights_01"
        flags: u8 = 132
    }
    "Maps/Particles/Snowdown/Snow_StartOfGame_Square" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 200
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[f32] = {
                            400
                            400
                            200
                            0
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
                lifetime: option[f32] = {
                    25
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
                                constantValue: f32 = 100
                            }
                            axisFraction: vec3 = { 1, 1, 0 }
                        }
                    }
                }
                emitterName: string = "SnowHighOnly"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -110, -100, 110 }
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
                            0.400000006
                            1
                        }
                        values: list[vec3] = {
                            { -330, -200, 220 }
                            { -220, -200, 220 }
                            { -110, -100, 110 }
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
                            constantValue: f32 = 1
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                particleColorTexture: string = "ASSETS/Shared/Particles/color-bellramp.TFT_SET4.dds"
                pass: i16 = 100
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 12, 12, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.600000024
                        }
                        values: list[vec3] = {
                            { 24, 24, 0 }
                            { 12, 12, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/Snowdown/Env_MB_snow_flakes.dds"
                uvMode: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 300
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[f32] = {
                            600
                            600
                            300
                            0
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
                lifetime: option[f32] = {
                    25
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
                                constantValue: f32 = 100
                            }
                            axisFraction: vec3 = { 1, 1, 0 }
                        }
                    }
                }
                emitterName: string = "Snow"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -110, -100, 110 }
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
                            0.400000006
                            1
                        }
                        values: list[vec3] = {
                            { -330, -200, 220 }
                            { -220, -200, 220 }
                            { -110, -100, 110 }
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
                            constantValue: f32 = 1
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                particleColorTexture: string = "ASSETS/Shared/Particles/color-bellramp.TFT_SET4.dds"
                pass: i16 = 100
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 12, 12, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.600000024
                        }
                        values: list[vec3] = {
                            { 24, 24, 0 }
                            { 12, 12, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/Snowdown/Env_MB_snow_flakes.dds"
                uvMode: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1000
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
                lifetime: option[f32] = {
                    8
                }
                isSingleParticle: flag = true
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
                                constantValue: f32 = 100
                            }
                            axisFraction: vec3 = { 1, 1, 0 }
                        }
                    }
                }
                emitterName: string = "SnowBurst"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -110, -100, 110 }
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
                            0.400000006
                            1
                        }
                        values: list[vec3] = {
                            { -330, -200, 220 }
                            { -220, -200, 220 }
                            { -110, -100, 110 }
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
                            constantValue: f32 = 1
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                particleColorTexture: string = "ASSETS/Shared/Particles/color-bellramp.TFT_SET4.dds"
                pass: i16 = 100
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 24, 24, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 24, 24, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/Snowdown/Env_MB_snow_flakes.dds"
                uvMode: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 25
                }
                isSingleParticle: flag = true
                emitterName: string = "Basic"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1200, 1200, 0 }
                }
                texture: string = "ASSETS/Shared/Particles/Thresh_Skin05_Z_Hold_01.dds"
            }
        }
        visibilityRadius: f32 = 2000
        particleName: string = "Snow_StartOfGame_Square"
        particlePath: string = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
    }
    "Maps/Particles/NexusBlitz/SRUAP_Order_BaseDoor_Shield_Bottom" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                childParticleSetDefinition: embed = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effect: link = "Maps/Particles/SR/SRU_Order_BaseDoor_Glow"
                        }
                        VfxChildIdentifier {
                            effect: link = "Maps/Particles/SR/SRU_Order_BaseDoor_GlowChild"
                        }
                        VfxChildIdentifier {
                            effect: link = "Maps/Particles/SR/SRU_Order_BaseDoor_GlowChild"
                        }
                    }
                    boneToSpawnAt: list[string] = {
                        "centershield"
                        "L_Shield"
                        "R_Shield"
                    }
                }
                emitterName: string = "Shield"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { -110, -25, 62 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Maps/Particles/NexusBlitz/NB_Gate.NexusBlitz_10_25_Release.skn"
                        mMeshSkeletonName: string = "ASSETS/Maps/Particles/NexusBlitz/NB_Gate.NexusBlitz_10_25_Release.skl"
                        mAnimationName: string = "ASSETS/Shared/Particles/SRUAP_Order_BaseDoor_Idle1.anm"
                    }
                }
                blendMode: u8 = 1
                pass: i16 = 5
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -16, -30 }
                }
                texture: string = "ASSETS/Maps/Particles/NexusBlitz/NB_Gate_Blue.dds"
            }
        }
        particleName: string = "SRUAP_Order_BaseDoor_Shield_Bottom"
        particlePath: string = "Maps/Particles/NexusBlitz/SRUAP_Order_BaseDoor_Shield_Bottom"
        assetRemappingTable: list[embed] = {
            VfxAssetRemap {
                oldAsset: hash = 0xef723b5a
                newAsset: string = "ASSETS/Maps/Particles/NexusBlitz/NB_Gate_Red.dds"
            }
        }
    }
    "Maps/Particles/NexusBlitz/SRUAP_Chaos_BaseDoor_Bottom" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
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
                    0.200000003
                }
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "AreaSphere"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_order_basedoor_barrier_areasphere2.scb"
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
                            { 0.800000012, 0.800000012, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 137, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Chaos_BaseDoor_Barrier.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00999999978, 0.200000003 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.00999999978, 0.200000003 }
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
                textureMult: string = "ASSETS/Shared/Particles/SRU_Chaos_BaseDoor_Barrier_Mult.dds"
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
                    constantValue: f32 = 0.899999976
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
                    0.200000003
                }
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "AreaDisc"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_order_basedoor_barrier_arearing.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.5, 0.5, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.5, 0.5, 1, 0 }
                            { 0.5, 0.5, 1, 1 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 137, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Chaos_BaseDoor_Barrier.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00999999978, -0.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.00999999978, -0.5 }
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
                textureMult: string = "ASSETS/Shared/Particles/SRU_Chaos_BaseDoor_Barrier_Mult.dds"
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
                    constantValue: f32 = 0.239999995
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
                                    0.800000012
                                    1.20000005
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
                particleLinger: option[f32] = {
                    0.5
                }
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "AreaRing"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_order_basedoor_barrier_areasphere.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 0.5, 1, 0.5, 0.200000003 }
                            { 1, 1, 1, 0.400000006 }
                            { 1, 1, 1, 0.297993004 }
                            { 0.300000012, 1, 0.300000012, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 137, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Chaos_BaseDoor_AreaRing.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00300000003, 0 }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
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
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
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
                            10
                        }
                    }
                }
                particleLinger: option[f32] = {
                    20
                }
                emitterName: string = "Mid_sparkles"
                birthVelocity: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 8, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 8, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                emissionMeshName: string = "ASSETS/Shared/Particles/sru_order_basedoor_barrier_meshemit4.NexusBlitz_10_25_Release.scb"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.701960802 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 0, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 0 }
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
                            { 50, 50, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 35, 35, 35 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
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
                            { 35, 35, 35 }
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
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Chaos_sparkles.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
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
                            10
                        }
                    }
                }
                particleLinger: option[f32] = {
                    20
                }
                emitterName: string = "Side_sparkles1"
                birthVelocity: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 8, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 8, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 0, -160 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
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
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 0, 0 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.701960802 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 0, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 0 }
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
                            { 50, 50, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 25, 25 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1
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
                            { 25, 25, 25 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Chaos_sparkles.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
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
                            10
                        }
                    }
                }
                particleLinger: option[f32] = {
                    20
                }
                emitterName: string = "Side_sparkles2"
                birthVelocity: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 8, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 8, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 26, 0, 160 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
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
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 0, 0 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.701960802 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 0, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 0 }
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
                            { 50, 50, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 25, 25 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1
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
                            { 25, 25, 25 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Chaos_sparkles.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
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
                particleLinger: option[f32] = {
                    17
                }
                emitterName: string = "structureGlow"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sruap_order_basedoor_glow.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.149019614 }
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.10000002, 1.10000002, 1.10000002 }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Chaos_Color.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.899999976
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
                    0.200000003
                }
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "OutSide_AreaDisc"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { -50, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_order_basedoor_barrier_arearing2.scb"
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
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 137, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Chaos_BaseDoor_Barrier.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00999999978, -0.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.00999999978, -0.5 }
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
                textureMult: string = "ASSETS/Shared/Particles/SRU_Chaos_BaseDoor_Barrier_Mult.dds"
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
        particleName: string = "SRUAP_Chaos_BaseDoor_Bottom"
        particlePath: string = "Maps/Particles/NexusBlitz/SRUAP_Chaos_BaseDoor_Bottom"
        assetRemappingTable: list[embed] = {
            VfxAssetRemap {
                oldAsset: hash = 0x8ced37d7
                newAsset: string = "ASSETS/Shared/Particles/SRU_Order_BaseDoor_Glow.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0x3975dea0
                newAsset: string = "ASSETS/Shared/Particles/SRU_Order_BaseDoor_Barrier_Mult.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0xd6c40879
                newAsset: string = "ASSETS/Shared/Particles/SRU_Order_BaseDoor_AreaRing.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0x297f0005
                newAsset: string = "ASSETS/Shared/Particles/SRU_Order_sparkles.dds"
            }
            VfxAssetRemap {
                newAsset: string = "ASSETS/Shared/Particles/SRU_Order_BaseDoor_GroundGlow_Top.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0x0d3a4feb
                newAsset: string = "ASSETS/Shared/Particles/SRU_Order_Color.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0xeb6a9f53
                newAsset: string = "ASSETS/Shared/Particles/SRU_Order_BaseDoor_Barrier.dds"
            }
        }
    }
    "Maps/Particles/NexusBlitz/SRUAP_Order_BaseDoor_Bottom" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
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
                    0.200000003
                }
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "AreaSphere"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_order_basedoor_barrier_areasphere2.scb"
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
                            { 0.800000012, 0.800000012, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 305, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Order_BaseDoor_Barrier.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00999999978, 0.200000003 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.00999999978, 0.200000003 }
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
                textureMult: string = "ASSETS/Shared/Particles/SRU_Order_BaseDoor_Barrier_Mult.dds"
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
                    constantValue: f32 = 1.5
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
                                    0.5
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
                    0.200000003
                }
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "AreaDisc"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_order_basedoor_barrier_arearing.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.5, 0.5, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.5, 0.5, 1, 0 }
                            { 0.5, 0.5, 1, 1 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 305, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Order_BaseDoor_Barrier.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00999999978, -0.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.00999999978, -0.5 }
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
                textureMult: string = "ASSETS/Shared/Particles/SRU_Order_BaseDoor_Barrier_Mult.dds"
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
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8
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
                            8
                        }
                    }
                }
                particleLinger: option[f32] = {
                    18
                }
                emitterName: string = "sparkles"
                birthVelocity: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 8, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 8, 0 }
                        }
                    }
                }
                emissionMeshName: string = "ASSETS/Shared/Particles/sru_order_basedoor_barrier_meshemit2.scb"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.701960802 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.768626988, 0.847059011, 0.87450999, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.768626988, 0.847059011, 0.87450999, 0 }
                            { 0.768626988, 0.847059011, 0.87450999, 1 }
                            { 0.768626988, 0.847059011, 0.87450999, 1 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 0 }
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
                            { 50, 50, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 35, 35, 35 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
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
                            { 35, 35, 35 }
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
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Order_sparkles.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
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
                            5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    15
                }
                emitterName: string = "structureGlow"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { -110, 50, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sruap_order_basedoor_glow.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.149019614 }
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
                texture: string = "ASSETS/Shared/Particles/SRU_Order_Color.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.239999995
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            7.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.5
                }
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "AreaRing"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_order_basedoor_barrier_areasphere.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 0.5, 1, 0.5, 0.349999994 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.975000024 }
                            { 0.300000012, 1, 0.300000012, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -55, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Order_BaseDoor_AreaRing.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00300000003, 0 }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
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
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 9
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
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
                            9
                        }
                    }
                }
                particleLinger: option[f32] = {
                    19
                }
                emitterName: string = "sparkles3"
                birthVelocity: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 8, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 8, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { -70, 0, 200 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
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
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.701960802 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.333332986, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 0 }
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
                            { 50, 50, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 25, 25 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1
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
                            { 25, 25, 25 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Order_sparkles.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
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
                                    0.5
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
                    0.200000003
                }
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "OutSide_AreaDisc"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_order_basedoor_barrier_arearing2.scb"
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
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 305, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Order_BaseDoor_Barrier.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00999999978, -0.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.00999999978, -0.5 }
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
                textureMult: string = "ASSETS/Shared/Particles/SRU_Order_BaseDoor_Barrier_Mult.dds"
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
                    constantValue: f32 = 0.100000001
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 16
                }
                particleLinger: option[f32] = {
                    26
                }
                emitterName: string = "structureGlow2"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { -166, -36.5, 13 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_order_basedoor_groundglow_top.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.5
                            0.949999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.474999994 }
                            { 1, 1, 1, 0.5 }
                            { 1, 1, 1, 0.5 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Order_BaseDoor_GroundGlow_Bottom.dds"
            }
        }
        particleName: string = "SRUAP_Order_BaseDoor_Bottom"
        particlePath: string = "Maps/Particles/NexusBlitz/SRUAP_Order_BaseDoor_Bottom"
        assetRemappingTable: list[embed] = {
            VfxAssetRemap {
                oldAsset: hash = 0x39708713
                newAsset: string = "ASSETS/Shared/Particles/SRU_Chaos_BaseDoor_Glow.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0xf34d1760
                newAsset: string = "ASSETS/Shared/Particles/SRU_Chaos_BaseDoor_Barrier_Mult.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0x13816339
                newAsset: string = "ASSETS/Shared/Particles/SRU_Chaos_BaseDoor_AreaRing.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0xf7c19ac5
                newAsset: string = "ASSETS/Shared/Particles/SRU_Chaos_sparkles.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0x0eaaba20
                newAsset: string = "ASSETS/Shared/Particles/SRU_Order_BaseDoor_GroundGlow_Bottom_red.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0xb24905ab
                newAsset: string = "ASSETS/Shared/Particles/SRU_Chaos_Color.dds"
            }
        }
    }
    "Maps/Particles/NexusBlitz/SRUAP_Chaos_BaseDoor_Shield_Bottom" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                childParticleSetDefinition: embed = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effect: link = "Maps/Particles/SR/SRU_Chaos_BaseDoor_Glow"
                        }
                        VfxChildIdentifier {
                            effect: link = "Maps/Particles/SR/SRU_Chaos_BaseDoor_GlowChild"
                        }
                        VfxChildIdentifier {
                            effect: link = "Maps/Particles/SR/SRU_Chaos_BaseDoor_GlowChild"
                        }
                    }
                    boneToSpawnAt: list[string] = {
                        "centershield"
                        "L_Shield"
                        "R_Shield"
                    }
                }
                emitterName: string = "Shield1"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 45, -65 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Maps/Particles/NexusBlitz/NB_Gate.NexusBlitz_10_25_Release.skn"
                        mMeshSkeletonName: string = "ASSETS/Maps/Particles/NexusBlitz/NB_Gate.NexusBlitz_10_25_Release.skl"
                        mAnimationName: string = "ASSETS/Shared/Particles/SRUAP_Order_BaseDoor_Idle1.anm"
                    }
                }
                blendMode: u8 = 1
                pass: i16 = 5
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, -20 }
                }
                texture: string = "ASSETS/Maps/Particles/NexusBlitz/NB_Gate_Red.dds"
            }
        }
        particleName: string = "SRUAP_Chaos_BaseDoor_Shield_Bottom"
        particlePath: string = "Maps/Particles/NexusBlitz/SRUAP_Chaos_BaseDoor_Shield_Bottom"
        assetRemappingTable: list[embed] = {
            VfxAssetRemap {
                oldAsset: hash = 0x0b370c0b
                newAsset: string = "ASSETS/Maps/Particles/NexusBlitz/NB_Gate_Blue.dds"
            }
        }
    }
    "Maps/MapGeometry/Map21/Chunks/OldMap_Meshes" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x017a8974 = null
            0xd7386c06 = null
            0xac58a0f3 = null
            0x77344913 = null
            0x566f0f6c = null
            0x883bf63f = null
            0x4f92208f = null
            0x0cbcab43 = null
            0x047ca4c2 = null
            0x3c35e9ad = null
            0x7aa7d7d9 = null
            0xce4744b2 = null
            0x6da24471 = null
            0xbd4fe7b3 = null
            0xeb758f79 = null
            0xab82e4fc = null
            0x2ea898f4 = null
            0xa1c1e164 = null
            0x0e1d5228 = null
            0x6661e54c = null
            0xe3025074 = null
            0xbceef32d = null
            0x9ab849a9 = null
            0xc1f60b75 = null
            0x7e36b9d3 = null
            0x1fd32624 = null
            0x8500ca72 = null
            0xdf75b3ba = null
            0x705d2d9d = null
            0x1a37011e = null
            0xd816fff1 = null
            0x8517ea1a = null
            0x4314343c = null
            0x5c079e08 = null
            0xf22630b7 = null
            0x6644102a = null
            0xae4ef37b = null
            0x8abfe89b = null
            0xfed2d270 = null
            0x5f803aa8 = null
            0x1e3e3ca8 = null
            0x52de8b30 = null
            0x3b70c487 = null
            0x71419d6f = null
            0x95f3e7e8 = null
            0xebb97636 = null
            0xc8ae84e2 = null
            0xd7007d38 = null
            0xe1765151 = null
            0x2be6c6a1 = null
            0x97cce524 = null
            0x08ce341f = null
            0x3cd8841c = null
            0x721b5ff3 = null
            0x6795029d = null
            0xc615ebb3 = null
            0x98933aeb = null
            0x6dcb4aa4 = null
            0x8296a9f5 = null
            0xd52c9b92 = null
            0x994ad7db = null
            0x4d7b95ee = null
            0x0e9a5a3e = null
            0xedafcd54 = null
            0x811b9dc2 = null
            0x58ab8afc = null
            0x0ce18f19 = null
            0xc0fdfc29 = null
            0x8bd13509 = null
            0xc3516b4f = null
            0x935bf4fe = null
            0x32783886 = null
            0x2780e53b = null
            0x0df93558 = null
            0x4618140a = null
            0xe363c277 = null
            0xefaaa93d = null
            0x7de8adcb = null
            0xcfdd554b = null
            0xdf26795d = null
            0x5e2a1957 = null
            0xfb864d0e = null
            0xe2025734 = null
            0x7ae10976 = null
            0xcc9b5072 = null
            0x02cda1f7 = null
            0x2ed9b5d8 = null
            0x6c0934fb = null
            0x77b6b74b = null
            0x587cc42c = null
            0xa378fe28 = null
            0x1e65066b = null
            0xa84ac87d = null
            0x4b2e25a8 = null
            0x0f081ba6 = null
            0xf70c8a1a = null
            0x77018707 = null
            0x7d818ef3 = null
            0xbee286e0 = null
            0xc274874c = null
            0xba301fd9 = null
            0x202aa631 = null
            0x88e57746 = null
            0xceb67033 = null
            0xfe66e3cd = null
            0xb43d6be2 = null
            0x0fe7b016 = null
            0x5103386b = null
            0xed2be437 = null
            0x14524838 = null
            0x97705176 = null
            0xe697661d = null
            0x8e1bce91 = null
            0x75411cf8 = null
            0x06249d95 = null
            0x55d927ee = null
            0x3a8fa0c8 = null
            0x673d8e90 = null
            0x93f0a5f2 = null
            0x81da0f65 = null
            0xda47bc3c = null
            0x347be2a7 = null
            0x8a7107ee = null
            0x58f20bfc = null
            0x25d0b28a = null
            0x37309e81 = null
            0xf12dcb2e = null
            0x66f78163 = null
            0x7428232c = null
            0x97569f0d = null
            0x74db8e7b = null
            0x3e66d077 = null
            0xc93845e7 = null
            0xfe91b40f = null
            0x230695a6 = null
            0xe49d1485 = null
            0xcced771e = null
            0xfd805e76 = null
            0x1d647afb = null
            0x95bef017 = null
            0x8341f4c3 = null
            0x0bdba7d1 = null
            0x113c74fd = null
            0x4e63f3a5 = null
            0x57417eb8 = null
            0x02af61fc = null
            0xac0a708d = null
            0x6a17c544 = null
            0x789b80fd = null
            0x360cc315 = null
            0xaf17bf32 = null
            0x6163148b = null
            0xb7e2d293 = null
            0x4ce24d6d = null
            0x17df840a = null
            0xed6bcd64 = null
            0x78449071 = null
            0xd06b27f2 = null
            0x0c6484fe = null
            0xd7360a39 = null
            0x7e840b5c = null
            0xeae3c38c = null
            0x2ad5c82f = null
            0xb2ea2ad5 = null
            0x3010b596 = null
            0x761ec120 = null
            0x356ae57c = null
            0xf4c771a8 = null
            0x7b6683af = null
            0x6545f54a = null
            0xe3cb5f61 = null
            0x10b34b93 = null
            0x8aa71d77 = null
            0x9914acc3 = null
            0x8cb5f8af = null
            0xf0008511 = null
            0xb8b6a4af = null
            0x610328d8 = null
            0x928366e1 = null
            0x52616e28 = null
            0x134387e7 = null
            0xd9e5b44d = null
            0x23a0ee89 = null
            0x4e69c259 = null
            0x037c08f8 = null
            0x888f23d7 = null
            0xbdedb30a = null
            0xef19f50f = null
            0x9c7644ff = null
            0x7408e0c8 = null
            0x5faff466 = null
            0xc8acaeb2 = null
            0xf8f381f7 = null
            0xbf24a1e1 = null
            0x699c8f1a = null
            0xb581a22c = null
            0x79d54b01 = null
            0xd587d9c2 = null
            0x9cf23e4b = null
            0x9fbafb0b = null
            0x20835d01 = null
            0x60616e6c = null
            0x33bea625 = null
            0x8b7d111f = null
            0x61e76caf = null
            0x988cdb74 = null
            0x7295b7aa = null
            0x88dcf74c = null
            0xe8c0b8ce = null
            0xbd25cb0b = null
            0x1b2dcbf6 = null
            0xf1a47f0c = null
            0xba47b3d2 = null
            0x53a0015e = null
            0xe6c3d344 = null
            0xa3a10cab = null
            0x8a38bd2e = null
            0x1622a6c5 = null
            0x74ee2103 = null
            0x449920a6 = null
            0xefce6b74 = null
            0x638987c0 = null
            0xb1f9b472 = null
            0x8f0d1049 = null
            0x7479426b = null
            0x548b671b = null
            0xc9243a48 = null
            0xde9b45f9 = null
            0xf98b0e8e = null
            0x63575aa4 = null
            0x7bce7b49 = null
            0xa7a61cf7 = null
            0xbed4910b = null
            0x2c3a6aa7 = null
            0xe8169195 = null
            0x01f158f1 = null
            0xd808c5c8 = null
            0x0583565d = null
            0x6e74c08f = null
            0x40d90f53 = null
            0x0dbad53c = null
            0x83eaa623 = null
            0xbde931d5 = null
            0x93c25a00 = null
            0x79d4327c = null
            0xc4aa09b3 = null
            0xfc18a115 = null
            0x35eb61b2 = null
            0x03d9b580 = null
            0x68762516 = null
            0x818b77b7 = null
            0x0dd9ce5e = null
            0x35b6af89 = null
            0xaa0691b3 = null
            0xdd478999 = null
            0x53ba74e6 = null
            0xed6d33dd = null
            0xf5645cb3 = null
            0x83a55cc5 = null
            0xed372566 = null
            0x74d6991c = null
            0xd4d7e40d = null
            0xc2ab631f = null
            0x1fccb5ad = null
            0xab13e91b = null
            0x1aa77936 = null
            0xca2698ac = null
            0x428464fb = null
            0x02ed9f8e = null
            0x33ca4b15 = null
            0xf0dec661 = null
            0x65beca99 = null
            0x77c3c0e8 = null
            0x3d4dacb9 = null
            0x136aac73 = null
            0x5ec7887b = null
            0x9a6c3852 = null
            0xbaba8069 = null
            0x80ddf1d6 = null
            0xcede1ad4 = null
            0xb7016904 = null
            0x01e8132b = null
            0xfbd78743 = null
            0x990ebb22 = null
            0x33973e94 = null
            0x1d7e59bb = null
            0x6213090d = null
            0x07c8ef53 = null
            0x99519c31 = null
            0x8a2a5249 = null
            0xe161139c = null
            0x53868cc1 = null
            0x13fa80bc = null
            0x7f7f3c21 = null
            0xe532a237 = null
            0x397884b0 = null
            0x8e47d26d = null
            0x76b8d668 = null
            0xc14ef5ca = null
            0x5c2a7637 = null
            0x651121ab = null
            0x8c27e3ff = null
            0xcb3ecfae = null
            0xa9e9dd89 = null
            0x5fb293fc = null
            0xfd90f4d1 = null
            0x2a46d616 = null
            0x9186b4af = null
            0x0ce6ea22 = null
            0x4caa2bec = null
            0x33ce9434 = null
            0xf4e40e63 = null
            0x6f21e4e2 = null
            0xf25fa38b = null
            0x89a42bb6 = null
            0x552962a3 = null
            0x28dc95bc = null
            0xce51b8c2 = null
            0xf6a53070 = null
            0xe19e2862 = null
            0x4da14fa0 = null
            0xd46785cc = null
            0xf529db7d = null
        }
        path: string = "Maps/MapGeometry/Map21/Chunks/OldMap_Meshes"
    }
    "Maps/MapGeometry/Map21/Chunks/Default" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x05a90d36 = MapGroup {
                members: list2[string] = {
                    "ca1408e7-5f3b-4c63-bc1d-8d9ac0b2bc2b"
                    "5b2ea12d-cb5f-48c5-b36a-f2f7f91f7a13"
                    "3c04e3eb-652e-4ea6-b3a3-54ddab4829c6"
                    "8f2e1b62-9f6a-43e7-8fa4-88770526e152"
                    "1c78e067-c0e9-4675-ab07-f60c49f2ddb4"
                }
                transform: mtx44 = {
                    0.710207522, 0, -0.703992426, 0
                    0, 1, 0, 0
                    0.703992426, 0, 0.710207522, 0
                    9948.59863, -8.33477783, 10202.8262, 1
                }
                name: string = "group1"
            }
            0x29b9dcee = MapGroup {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4923.08398, -81.8805847, 8200.27637, 1
                }
                name: string = "Jungle_Tower_Group"
            }
            0x2ab705ea = MapGroup {
                members: list2[string] = {
                    "10b3a631-c932-44e6-b019-e27687e8900f"
                    "c2cd20e0-793f-4fe3-830e-77381fcee220"
                }
                transform: mtx44 = {
                    0.846463799, 0, -0.532446265, 0
                    0, 1, 0, 0
                    0.532446265, 0, 0.846463799, 0
                    5557.94385, -72.2928162, 7063.74121, 1
                }
                name: string = "OrderRaptorBrushGroup"
            }
            0x0dbbda5c = MapGroup {
                transform: mtx44 = {
                    0.955833793, 0, 0.293907851, 0
                    0, 1, 0, 0
                    -0.293907851, 0, 0.955833793, 0
                    9288.53125, -70.6081238, 7078.81641, 1
                }
                name: string = "ChaosRaptorBrushGroup"
            }
            0x43cb262e = MapGroup {
                transform: mtx44 = {
                    -1.0382359, -0, -0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8651.37305, -8381.14453, 2867.93848, 1
                }
                name: string = "group2"
            }
            0x015a6161 = MapGroup {
                transform: mtx44 = {
                    -0.983744323, -0, 0.0792123824, 0
                    0, 1, 0, 0
                    0.0802615359, 0, 0.996773839, 0
                    3388.76147, -117.025024, 10518.0654, 1
                }
                name: string = "group3"
            }
            0x5ff106db = MapGroup {
                members: list2[string] = {
                    "7a742618-fd8a-467b-a511-8262cf33e088"
                }
                transform: mtx44 = {
                    -0.924702942, -0, -0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11394.9043, -134.944687, 8116.81885, 1
                }
                name: string = "group4"
            }
            0x847eaa1a = MapGroup {
                transform: mtx44 = {
                    -1.04663467, -0, -0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10433.1084, -152.868439, 7328.06494, 1
                }
                name: string = "group5"
            }
            0x3585e0ab = MapGroup {
                transform: mtx44 = {
                    0.883206964, 0, -0.468983382, 0
                    0, 1, 0, 0
                    0.468983382, 0, 0.883206964, 0
                    3838.73608, -93.6594849, 8915.49121, 1
                }
                name: string = "group6"
            }
            0xf980dd7f = MapGroup {
                transform: mtx44 = {
                    0.927076697, 0, 0.374871641, 0
                    0, 1, 0, 0
                    -0.374871641, 0, 0.927076697, 0
                    718.888245, -230.86084, 8554.04199, 1
                }
                name: string = "group7"
            }
            0x3eec8532 = MapGroup {
                members: list2[string] = {
                    "6cf6fb10-be3a-4399-8c93-23a0d261fce1"
                    "00b47db2-f607-4991-9b05-4b2017f219d1"
                }
                transform: mtx44 = {
                    1.18691278, 0, 0.377589017, 0
                    0, 1.24552619, 0, 0
                    -0.377589017, 0, 1.18691278, 0
                    99.7592468, -85.8916626, 9754.12598, 1
                }
                name: string = "group8"
            }
            0xf067784a = MapGroup {
                members: list2[string] = {
                    "adf39ced-d1b4-4142-a445-ba216e9bd236"
                    "5f878881-212c-4c1e-becb-d1ae390d4418"
                }
                transform: mtx44 = {
                    0.870510578, 0, 0.492149651, 0
                    0, 1, 0, 0
                    -0.492149651, 0, 0.870510578, 0
                    -1795.06543, -6899.30322, 9145.97656, 1
                }
                name: string = "group9"
            }
            0xa4ee783f = MapGroup {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3679.80493, -188.54657, 7850.1167, 1
                }
                name: string = "group10"
            }
            0xd10ba715 = MapGroup {
                transform: mtx44 = {
                    -1.00542259, -0, -0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11263.0508, -188.546326, 7821.34912, 1
                }
                name: string = "group11"
            }
            0xe74e9580 = MapGroup {
                transform: mtx44 = {
                    1.16776788, 0, 0, 0
                    0, 1.16776788, 0, 0
                    0, 0, 1.16776788, 0
                    10772.2852, -98.0845184, 7257.19971, 1
                }
                name: string = "group12"
            }
            0x102b4bbc = MapGroup {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2906.63281, 101.460365, 9853.07715, 1
                }
                name: string = "group13"
            }
            0x17b0941d = MapGroup {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2906.63281, 101.460365, 9853.07715, 1
                }
                name: string = "group14"
            }
            0xe1957a0e = MapGroup {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3735.45532, -148.266541, 10228.1426, 1
                }
                name: string = "group15"
            }
            0xda994ba7 = MapGroup {
                members: list2[string] = {
                    "ca8bdd67-6891-44a4-9c05-302cdb87e740"
                    "79a6f9f3-c44d-4414-b45b-ff3a82d9d735"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3735.45532, -148.266541, 10228.1426, 1
                }
                name: string = "group16"
            }
            0xe9f1c2e8 = MapGroup {
                members: list2[string] = {
                    "ae6342c9-8b2b-4a36-b567-867cf1b59b9b"
                }
                transform: mtx44 = {
                    -1.00594628, -0, -0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11189.0186, -148.266541, 10228.1426, 1
                }
                name: string = "group17"
            }
            0x31f57021 = MapGroup {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5921.2793, -100.144928, 6164.6665, 1
                }
                name: string = "group18"
            }
            0xc75390a2 = MapGroup {
                transform: mtx44 = {
                    -0.891199827, -0, -0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9028.6875, -100.144928, 6164.6665, 1
                }
                name: string = "group19"
            }
            0x796eb1fd = MapGroup {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4920.21728, -98.0847931, 5880.15137, 1
                }
                name: string = "group20"
            }
            0x34f0e824 = MapGroup {
                transform: mtx44 = {
                    -0.954379559, -0, 0.093158409, 0
                    0, 1, 0, 0
                    0.0971497595, 0, 0.995269775, 0
                    10063.998, -98.0849152, 5785.23926, 1
                }
                name: string = "group21"
            }
            0x6921c055 = MapGroup {
                members: list2[string] = {
                    "8770d91e-7268-442b-b119-15c8238fbd6f"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6422.5249, -145.358368, 4688.46924, 1
                }
                name: string = "group22"
            }
            0x9bcbf89c = MapGroup {
                members: list2[string] = {
                    "d52ce398-a627-4a9b-887b-e98ad5726019"
                }
                transform: mtx44 = {
                    -1.061239, -0, -0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8605.27637, -145.358368, 4734.85107, 1
                }
                name: string = "group23"
            }
            0xe0797b56 = MapGroup {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2116.11621, -967.270874, 5628.26904, 1
                }
                name: string = "group24"
            }
            0xec679476 = MapGroup {
                transform: mtx44 = {
                    -1.03230512, -0, -0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12852.8008, -967.270386, 5662.44287, 1
                }
                name: string = "group25"
            }
            0xb29ce3db = MapGroup {
                members: list2[string] = {
                    "7ef346a9-5fce-49d3-a7bf-9c52af4115a0"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3570.07104, -313.555573, 3239.8706, 1
                }
                name: string = "group26"
            }
            0x9976ca83 = MapGroup {
                transform: mtx44 = {
                    -0.899686694, -0, -0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11226.2891, -313.555573, 3239.8706, 1
                }
                name: string = "group27"
            }
            0x97d32bb8 = MapGroup {
                transform: mtx44 = {
                    -0.899020374, 0.161987737, 0.250451952, 0
                    0.164742649, 0.985268235, -0.0458945334, 0
                    0.268364072, 0, 0.963317573, 0
                    8425.60156, -64.4485168, 2717.95508, 1
                }
                name: string = "group28"
            }
            0x262356c2 = MapGroup {
                transform: mtx44 = {
                    -0.899020374, 0.161987737, 0.250451952, 0
                    0.164742649, 0.985268235, -0.0458945334, 0
                    0.268364072, 0, 0.963317573, 0
                    9195.64648, -196.638947, 2932.15234, 1
                }
                name: string = "group29"
            }
            0xced37ec8 = MapGroup {
                transform: mtx44 = {
                    0.839504838, 0, -0.540427446, 0
                    0, 1, 0, 0
                    0.541286051, 0, 0.840838552, 0
                    8488.01953, -90.6315689, 10235.5312, 1
                }
                name: string = "group30"
            }
            0x030a9995 = MapGroup {
                transform: mtx44 = {
                    -0.849395752, -0.0570810772, -0, 0
                    -0.0670507476, 0.997749567, 0, 0
                    0, 0, 1, 0
                    6306.35644, -86.6927185, 8188.85742, 1
                }
                name: string = "group31"
            }
            0x07606352 = MapGroup {
                transform: mtx44 = {
                    0.629659057, 0, -0.776871622, 0
                    0, 1, 0, 0
                    0.776871622, 0, 0.629659057, 0
                    7535.02637, -171.658112, 5280.51611, 1
                }
                name: string = "group32"
            }
            0x90e5faab = MapGroup {
                transform: mtx44 = {
                    -1.10756874, -0, -0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10016.8926, -152.833878, 9163.74707, 1
                }
                name: string = "group33"
            }
            0x689545bc = MapGroup {
                transform: mtx44 = {
                    0.143059999, 0, 0.989714146, 0
                    0, 1, 0, 0
                    -0.989714146, 0, 0.143059999, 0
                    5680.43457, -77.1534424, -1029.61182, 1
                }
                name: string = "group35"
            }
            0x2af50ffe = MapGroup {
                members: list2[string] = {
                    "402f8a58-1b71-4fd7-bf8a-9c2924992fb9"
                    "6f3979d5-c839-49c4-b40c-a13b055ecbc6"
                    "8dac6851-3584-48ba-ae56-b9f7141113b1"
                    "873b9fb6-5e95-47de-bf50-51fa11001949"
                }
                transform: mtx44 = {
                    0.631147861, 0, -0.775662541, 0
                    0, 1, 0, 0
                    0.775662541, 0, 0.631147861, 0
                    8066.65332, -77.1290283, 6274.31543, 1
                }
                name: string = "group36"
            }
            0xa0eea6ea = MapGroup {
                members: list2[string] = {
                    "7728c65b-8446-4744-9e94-695edb9a9007"
                    "5534b74b-1d9b-47b9-9440-22d10a47d8fe"
                    "d913b18f-3e45-40bd-87da-cae680ab0812"
                    "ee749749-b8c3-4720-895b-310e177d31ef"
                }
                transform: mtx44 = {
                    0.998663127, 0, 0.0516909063, 0
                    0, 1, 0, 0
                    -0.0516909063, 0, 0.998663127, 0
                    7242.9873, -77.1286316, 6370.33154, 1
                }
                name: string = "group37"
            }
            0x5c091431 = MapGroup {
                members: list2[string] = {
                    "a6289bf8-e1cc-46e5-96c3-946631d1a403"
                    "356dc02c-b6cc-4503-ba8b-b7a5f8df44b8"
                    "51d6c9d8-5b98-4ce9-8bb0-c019afea4557"
                }
                transform: mtx44 = {
                    0.576277375, 0, -0.817254186, 0
                    0, 1, 0, 0
                    0.817254186, 0, 0.576277375, 0
                    6523.2002, -77.1296997, 3235.24805, 1
                }
                name: string = "group38"
            }
            0x814cf1a2 = MapGroup {
                transform: mtx44 = {
                    0.997552693, 0, 0.0699188486, 0
                    0, 1, 0, 0
                    -0.0699188486, 0, 0.997552693, 0
                    8572.2373, -79.4921265, 3253.3833, 1
                }
                name: string = "group39"
            }
            0x65c96447 = MapGroup {
                transform: mtx44 = {
                    0.812140048, 0, -0.583462536, 0
                    0, 1, 0, 0
                    0.583462536, 0, 0.812140048, 0
                    5568.67725, -77.1296997, 9997.41699, 1
                }
                name: string = "group34"
            }
            0xaf418124 = MapGroup {
                transform: mtx44 = {
                    0.507142186, 0, -0.861862421, 0
                    0, 1, 0, 0
                    0.861862421, 0, 0.507142186, 0
                    10116.8184, -77.1303101, 9843.5127, 1
                }
                name: string = "group40"
            }
            0xdf77b4b2 = MapGroup {
                transform: mtx44 = {
                    0.978669941, 0, -0.205438927, 0
                    0, 1, 0, 0
                    0.205438927, 0, 0.978669941, 0
                    9483.68164, -77.1292038, 7843.73193, 1
                }
                name: string = "group41"
            }
            0x4673ff50 = MapGroup {
                members: list2[string] = {
                    "9fb63cea-a6c7-4743-a069-b80538d6797c"
                    "0b918fee-2cfd-4096-b794-16e23df0d5b4"
                    "4124638a-47e0-4373-9795-e0e73993a393"
                    "37742e23-993e-4f9c-81d9-4293639b88c8"
                    "94b777c1-4ec1-4d1d-8e98-67d3e5b89556"
                }
                transform: mtx44 = {
                    0.982829928, 0, -0.184513777, 0
                    0, 1, 0, 0
                    0.184513777, 0, 0.982829928, 0
                    7414.43408, -77.1253586, 9835.89941, 1
                }
                name: string = "group42"
            }
            0xcd37c1ba = MapGroup {
                members: list2[string] = {
                    "17ee6779-c3de-4717-8caf-90da5d72c070"
                    "d409716c-6885-4034-9048-0340d60f883c"
                    "17791be7-39f5-40e2-a187-db8d10653b0a"
                    "8d2d490b-48be-4964-a7d0-99b231f1e6ce"
                    "e1462fb1-fb73-48e3-9aee-f44659b4c71d"
                    "b7b9f982-abd7-48e9-a9fd-4809b3c679de"
                }
                transform: mtx44 = {
                    0.82639122, 0, 0.563096404, 0
                    0, 1, 0, 0
                    -0.563096404, 0, 0.82639122, 0
                    7267.85889, -77.1281662, 8344.4834, 1
                }
                name: string = "group43"
            }
            0x441f13a3 = MapGroup {
                members: list2[string] = {
                    "5e0fe32d-a3da-4ebb-a82a-8e66dea8a985"
                }
                transform: mtx44 = {
                    0.977624059, 0, -0.210359722, 0
                    0, 1, 0, 0
                    0.210359722, 0, 0.977624059, 0
                    7998.32275, -79.4910889, 8200.04492, 1
                }
                name: string = "group44"
            }
            0x0821158b = null
            0xba6b7b13 = null
            0x0d304638 = null
            0x6a197e94 = null
            0x118b456d = null
            0xc0e4372f = null
            0xc3e3ccba = null
            0xa487d9c0 = null
            0x6e8d7572 = null
            0xce8feec8 = null
            0x420efb27 = null
            0xe15f674e = null
            0xfbb586d4 = null
            0xc6769697 = null
            0xedfbfc6e = null
            0x0d72fd67 = null
            0x84e0d6f4 = null
            0x2e22d9af = null
            0x309a7f33 = null
            0x03da771d = null
            0xaa82c2cd = null
            0x3cf56feb = null
            0x068fdd9c = null
            0xf0486bea = null
            0x482cb365 = null
            0x0b72a8fd = null
            0xba64fa5f = null
            0x01fa0acf = null
            0x1ce49f63 = null
            0xc73229af = null
            0x92f4bab3 = null
            0xfc080a12 = null
            0x8a3fe429 = null
            0xa1dd16b9 = null
            0x38311f64 = null
            0x88fa0698 = null
            0x04eb92b5 = MapGroup {
                transform: mtx44 = {
                    0.99226737, 0, 0.124118328, 0
                    0, 1, 0, 0
                    -0.124118328, 0, 0.99226737, 0
                    644.606445, -12.936142, 8877.31641, 1
                }
                name: string = "group45"
            }
            0xfe7ea49e = null
            0x4fb00818 = null
            0xa6446a1c = null
            0xd5425b7e = null
            0x9151d4f2 = null
            0x36da0e6c = null
            0x7a05fbb3 = null
            0xfed103cd = null
            0x9138756b = null
            0x20c382c0 = null
            0x50443107 = null
            0x75eba6b3 = null
            0x374045ee = null
            0xce232caf = null
            0xa636350d = null
            0xc58e9cab = null
            0x9c201e53 = MapGroup {
                transform: mtx44 = {
                    0.904965341, 0, -0.425485343, 0
                    0, 1, 0, 0
                    0.425485343, 0, 0.904965341, 0
                    14428.7109, -6.87670135, 8847.7666, 1
                }
                name: string = "group46"
            }
            0xfa9bca2f = null
            0xd421bd8d = null
            0x5f9ecacc = null
            0x9d432482 = null
            0x598665d7 = null
            0xde360029 = null
            0x5696fe3a = MapGroup {
                transform: mtx44 = {
                    -0.996383905, 0, 0.0849735439, 0
                    0, 1, 0, 0
                    -0.0849735439, 0, -0.996383905, 0
                    14835.6221, -9.94563293, 8163.36084, 1
                }
                name: string = "group47"
            }
            0xf261b3f8 = MapGroup {
                transform: mtx44 = {
                    -0.414521486, 0, -0.910039723, 0
                    0, 1, 0, 0
                    0.910039723, 0, -0.414521486, 0
                    14702.3955, 190.929352, 8938.31152, 1
                }
                name: string = "group48"
            }
            0xe8c26394 = null
            0xddc6da92 = MapGroup {
                transform: mtx44 = {
                    0.824351907, 0, -0.56607759, 0
                    0, 1, 0, 0
                    0.56607759, 0, 0.824351907, 0
                    14196.2686, 237.396881, 9144.89453, 1
                }
                name: string = "group49"
            }
            0xfbbcdca1 = null
            0x913b8317 = null
            0x6e6fa09b = null
            0xf2e9ea8a = null
            0xfdd9df63 = null
            0xe39d376c = MapGroup {
                transform: mtx44 = {
                    -0.887596607, 0, -0.46062237, 0
                    0, 1, 0, 0
                    0.46062237, 0, -0.887596607, 0
                    14845.0293, -28.3274536, 8077.85938, 1
                }
                name: string = "group50"
            }
            0x64b69964 = MapGroup {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    14881.918, -43.9299927, 8028.86328, 1
                }
                name: string = "group51"
            }
            0xce3400b7 = null
            0x5f98a869 = null
            0xbf5e5b9b = null
            0xbc9dba2f = null
            0xf1d1a316 = null
            0xabc4d672 = null
            0x78d28b5c = null
            0x89bf3c1c = null
            0xef673b81 = null
            0x9eb9e9f6 = null
            0xe5fbea6c = null
            0xa1a8d942 = null
            0xc466d57a = null
            0xc99a9e9b = null
            0xd5bb6233 = null
            0x38453ae7 = null
            0xdd2deb57 = null
            0x214f46e1 = null
            0xc865fa0d = null
            0xafd243d0 = null
            0x7d2bf9ae = null
            0x8137e8ad = null
            0x6c946452 = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3511.76392, 18.2006531, 7926.29883, 1
                }
                name: string = "Snow_StartOfGame_Circle2"
            }
            0x96c7bc34 = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8299.25195, 18.2006531, 7918.59082, 1
                }
                name: string = "Snow_StartOfGame_Circle3"
            }
            0x9c6a3649 = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5904.09668, 18.2006531, 7922.89453, 1
                }
                name: string = "Snow_StartOfGame_Circle4"
            }
            0xe2d1f306 = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    13067.377, 18.2006531, 7916.96387, 1
                }
                name: string = "Snow_StartOfGame_Circle5"
            }
            0x93a9ed18 = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10672.2217, 18.2006531, 7921.26758, 1
                }
                name: string = "Snow_StartOfGame_Circle6"
            }
            0xb0e5beae = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    15459.2002, 18.2006531, 7833.12793, 1
                }
                name: string = "Snow_StartOfGame_Circle7"
            }
            0x2a5aeec4 = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3511.76392, 18.2006531, 5519.80957, 1
                }
                name: string = "Snow_StartOfGame_Circle8"
            }
            0x374f62e6 = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10672.2217, 18.2006531, 5514.77832, 1
                }
                name: string = "Snow_StartOfGame_Circle9"
            }
            0xbd6b4c2c = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    15459.2002, 18.2006531, 5426.63867, 1
                }
                name: string = "Snow_StartOfGame_Circle10"
            }
            0x3c378d6e = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    13067.377, 18.2006531, 5510.47461, 1
                }
                name: string = "Snow_StartOfGame_Circle11"
            }
            0x14935ae2 = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8299.25195, 18.2006531, 5512.10156, 1
                }
                name: string = "Snow_StartOfGame_Circle13"
            }
            0x537ff9f7 = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5904.09668, 18.2006531, 5516.40527, 1
                }
                name: string = "Snow_StartOfGame_Circle14"
            }
            0x158abad7 = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8299.25195, 18.2006531, 3114.11035, 1
                }
                name: string = "Snow_StartOfGame_Circle15"
            }
            0x76fb2bee = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3511.76392, 18.2006531, 3121.81836, 1
                }
                name: string = "Snow_StartOfGame_Circle16"
            }
            0x82f9229f = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    15459.2002, 18.2006531, 3028.64746, 1
                }
                name: string = "Snow_StartOfGame_Circle17"
            }
            0x75e7975a = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5904.09668, 18.2006531, 3118.41406, 1
                }
                name: string = "Snow_StartOfGame_Circle18"
            }
            0x65980ec5 = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1116.60913, 18.2006531, 3126.12207, 1
                }
                name: string = "Snow_StartOfGame_Circle19"
            }
            0x00f6d8f0 = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10672.2217, 18.2006531, 3116.78711, 1
                }
                name: string = "Snow_StartOfGame_Circle20"
            }
            0x57dba9d9 = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    13067.377, 18.2006531, 3112.4834, 1
                }
                name: string = "Snow_StartOfGame_Circle21"
            }
            0xdc44859e = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1116.60913, 18.2006531, 10318.0898, 1
                }
                name: string = "Snow_StartOfGame_Circle22"
            }
            0xc5eace36 = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    13067.377, 18.2006531, 10304.4512, 1
                }
                name: string = "Snow_StartOfGame_Circle23"
            }
            0x5e37a3a5 = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    15459.2002, 18.2006531, 10220.6152, 1
                }
                name: string = "Snow_StartOfGame_Circle24"
            }
            0xeb8a9cbb = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10672.2217, 18.2006531, 10308.7539, 1
                }
                name: string = "Snow_StartOfGame_Circle25"
            }
            0xf2eaf97e = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3511.76392, 18.2006531, 10313.7852, 1
                }
                name: string = "Snow_StartOfGame_Circle26"
            }
            0x270b8692 = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5904.09668, 18.2006531, 10310.3808, 1
                }
                name: string = "Snow_StartOfGame_Circle27"
            }
            0xbb946d0a = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8299.25195, 18.2006531, 10306.0781, 1
                }
                name: string = "Snow_StartOfGame_Circle28"
            }
            0x9c442643 = MapParticle {
                system: link = "Maps/Particles/SR/Sru_braziers_fire"
                transform: mtx44 = {
                    2, 0, 0, 0
                    0, 2, 0, 0
                    0, 0, 2, 0
                    7370.26709, 25.499033, 10562.2305, 1
                }
                name: string = "Sru_braziers_fire3"
            }
            0x128884ed = MapParticle {
                system: link = "Maps/Particles/SR/Sru_braziers_fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7513.771, 151.527298, 10761.3848, 1
                }
                name: string = "Sru_braziers_fire4"
            }
            0x7d2d0598 = MapPointLight {
                type: link = 0xf695f759
                radiusScale: f32 = 0.958000004
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7402.65576, 69.5488586, 10553.8057, 1
                }
                name: string = "nb_orange_01_3"
            }
            0xccc573e4 = MapPointLight {
                type: link = 0xf695f759
                radiusScale: f32 = 0.958000004
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7550.6665, 252.517731, 10698.6875, 1
                }
                name: string = "nb_orange_01_4"
            }
            0x79dc5d2e = MapParticle {
                system: link = "Maps/Particles/Snowdown/SRU_Snowdown_TreeLights_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4483.65234, -22.1306458, 7231.49756, 1
                }
                name: string = "SRU_Snowdown_TreeLights_01_1"
            }
            0x7a328bb7 = MapParticle {
                system: link = "Maps/Particles/Snowdown/SRU_Snowdown_TreeLights_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6320.79004, -14.2491608, 8371.83691, 1
                }
                name: string = "SRU_Snowdown_TreeLights_01_2"
            }
            0xc398ed80 = MapParticle {
                system: link = "Maps/Particles/Snowdown/SRU_Snowdown_TreeLights_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2466.77075, -14.249649, 9012.25391, 1
                }
                name: string = "SRU_Snowdown_TreeLights_01_3"
            }
            0xb6f374e0 = MapParticle {
                system: link = "Maps/Particles/Snowdown/SRU_Snowdown_TreeLights_02"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10148.9746, 191.913559, 10380.7363, 1
                }
                name: string = "SRU_Snowdown_TreeLights_02_1"
            }
            0x28c47a24 = MapParticle {
                system: link = "Maps/Particles/Snowdown/SRU_Snowdown_TreeLights_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10221.1719, -14.2494659, 5761.26514, 1
                }
                name: string = "SRU_Snowdown_TreeLights_01_4"
            }
            0xa139b636 = MapParticle {
                system: link = "Maps/Particles/Snowdown/SRU_Snowdown_TreeLights_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9434.2959, 98.7265015, 7333.99365, 1
                }
                name: string = "SRU_Snowdown_TreeLights_01_5"
            }
            0xccf045da = MapParticle {
                system: link = "Maps/Particles/Snowdown/SRU_Snowdown_TreeLights_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12597.3047, 23.5277557, 9152.04297, 1
                }
                name: string = "SRU_Snowdown_TreeLights_01_6"
            }
            0xbaa0969e = MapParticle {
                system: link = "Maps/Particles/Snowdown/SRU_Snowdown_TreeLights_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7326.98193, -13.1396561, 5273.52295, 1
                }
                name: string = "SRU_Snowdown_TreeLights_01_7"
            }
            0xff6c03d3 = MapParticle {
                system: link = "Maps/Particles/Snowdown/SRU_Snowdown_TreeLights_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5252.66064, -112.270752, 5203.11523, 1
                }
                name: string = "SRU_Snowdown_TreeLights_01_8"
            }
            0x36e66fea = MapParticle {
                system: link = "Maps/Particles/Snowdown/SRU_Snowdown_TreeLights_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7322.18262, 31.5661621, 2893.69726, 1
                }
                name: string = "SRU_Snowdown_TreeLights_01_9"
            }
            0x573e3c64 = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1126.875, 18.2006531, 7926.29883, 1
                }
                name: string = "Snow_StartOfGame_Circle1"
            }
        }
        path: string = "Maps/MapGeometry/Map21/Chunks/Default"
    }
    "Maps/MapGeometry/Map21/Chunks/Locators" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x169c519b = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9754.0127, -46.0064392, 7775.875, 1
                }
                name: string = "SLIME_BE_Chaos_Start2"
            }
            0x89fffd33 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6251.38525, -46.0000916, 6972.60596, 1
                }
                name: string = "SLIME_BE_Order_End5"
            }
            0xf3bc3e44 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7599.98535, -35.4170837, 6769.23975, 1
                }
                name: string = "SLIME_PushCartCenterLocator1"
            }
            0x7ce02544 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    13101.2392, -46.006073, 7664.56055, 1
                }
                name: string = "SLIME_KingPoroChaos"
            }
            0x6a12962f = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    13344.6953, -46.0030212, 8311.88086, 1
                }
                name: string = "SLIME_BE_Chaos_Start3"
            }
            0xb883d051 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999969602, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969602, 0
                    13806.3506, 32.1996155, 9898.58008, 1
                }
                name: string = "SLIME_FountainLaserSpawn_Right"
            }
            0x2104a5df = GdsMapObject {
                boxMin: vec3 = { 1784.94556, -41.4744263, 7711.83642 }
                boxMax: vec3 = { 1879.56763, 242.251465, 7806.4585 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    1432.25696, -41.473999, 7650.14697, 1
                }
                name: string = "__P_Order_Spawn_Barracks__R01"
            }
            0xac98238e = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    2800.00684, -30.8929749, 6791.1958, 1
                }
                name: string = "SLIME_BR_Order_Nexus"
            }
            0x565b69ed = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9436.77246, -46.0037537, 5759.31982, 1
                }
                name: string = "SLIME_BE_Chaos_End5"
            }
            0xc326d54f = GdsMapObject {
                boxMin: vec3 = { 13233.8916, -41.4789429, 7681.35547 }
                boxMax: vec3 = { 13328.5146, 242.246948, 7775.97754 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    13681.2031, -41.4790001, 7650.14697, 1
                }
                name: string = "__P_Chaos_Spawn_Barracks__R01"
            }
            0x15b09183 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    4976.52588, -43.7480011, 4174.72119, 1
                }
                name: string = "LootGoblinBotLaneLeft"
            }
            0x8eebbe41 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7202.94971, -45.9996033, 5143.56982, 1
                }
                name: string = "SLIME_BE_Order_End2"
            }
            0x78be4b67 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    9628.91992, -41.4783325, 8773.47852, 1
                }
                name: string = "SLIME_TurretFacing_RJ"
            }
            0x50eaa641 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9074.7793, -35.4132996, 8302.67871, 1
                }
                name: string = "SLIME_DraftRacingGoal_Chaos2"
            }
            0xdeff7496 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    4139.44824, -41.4758911, 6200.94434, 1
                }
                name: string = "SLIME_TurretFacing_LI_BOT"
            }
            0xc616ccf4 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10843.0576, -46.0032654, 6259.35742, 1
                }
                name: string = "SLIME_BE_Chaos_Start5"
            }
            0x094941fb = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11094.5801, -46.0052185, 6038.55078, 1
                }
                name: string = "SLIME_BE_Chaos_End6"
            }
            0x398cdfc1 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    6755.25098, -41.4767456, 9684.00781, 1
                }
                name: string = "LootGoblinHeraldPitLeft"
            }
            0x37b5eb66 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    8847.49707, -41.4783325, 6835.89795, 1
                }
                name: string = "SLIME_TurretFacing_RO"
            }
            0x522c6350 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8368.98438, -35.4180603, 3796.94287, 1
                }
                name: string = "SLIME_BR_Neutral_Bot2"
            }
            0x43d840e0 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    12173.7314, -43.7540588, 7840.51318, 1
                }
                name: string = "SLIME_TurretFacing_RN"
            }
            0x7476a2e4 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5258.14404, -35.4173279, 4773.09082, 1
                }
                name: string = "SLIME_DraftRacingGoal_Order1"
            }
            0xea1ec34b = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4839.4668, -46.0018005, 7727.08936, 1
                }
                name: string = "SLIME_BE_Order_End1"
            }
            0x032a0296 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999969602, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969602, 0
                    13499.4648, 32.2008362, 9211.46191, 1
                }
                name: string = "SLIME_FountainLocator_Right"
            }
            0x2d9ebd41 = MapLocator {
                0xad304db5: string = "Characters/URF_Feeneypult/Skins/Skin1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.430370033, 0.00506172702, -0.902640522, 0
                    -0.00517356349, 0.999954045, 0.00807413459, 0
                    0.902639925, 0.00814472884, -0.430324018, 0
                    1245.55212, -41.4775391, 8811.31348, 1
                }
                name: string = "SLIME_FeeneypultOrder"
            }
            0xe5aa3981 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    6618.40039, -30.8929749, 3681.21436, 1
                }
                name: string = "SLIME_BR_Order_Lower_Outer_South"
            }
            0x3bb12435 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    1736.16248, 32.1990013, 9211.57031, 1
                }
                name: string = "SLIME_FountainLocator_Left"
            }
            0xfa87e15d = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    7621.3584, -41.4752808, 5499.53564, 1
                }
                name: string = "SLIME_Map_Midpoint"
            }
            0x5f55b930 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8719.22852, -35.4165955, 9063.6582, 1
                }
                name: string = "SLIME_BR_Neutral_RightIsland"
            }
            0xc967c767 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999969602, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969602, 0
                    849.123535, 32.1977844, 11080.9404, 1
                }
                name: string = "SLIME_FountainLaserSpawn_Left"
            }
            0x838a08e3 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6609.64795, -35.4165955, 9626.96094, 1
                }
                name: string = "SLIME_BR_Neutral_LeftPassage"
            }
            0xd4c5a0a8 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6763.30029, -35.415863, 6291.27197, 1
                }
                name: string = "SLIME_BR_Neutral_LeftCase"
            }
            0xba9d41af = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5442.36133, -46.0022888, 5218.99072, 1
                }
                name: string = "SLIME_BE_Order_End3"
            }
            0x22dd67e3 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12371.6465, -35.4207458, 6903.94971, 1
                }
                name: string = "SLIME_BR_Chaos_Nexus"
            }
            0x173870b1 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    5027.4082, -41.4738159, 6652.07373, 1
                }
                name: string = "LootGoblinLeftEdge"
            }
            0xec9e20b5 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    2494.33228, -41.4768677, 7354.7793, 1
                }
                name: string = "SLIME_TurretFacing_LN_BOT"
            }
            0x525858db = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5954.77295, -35.4146423, 8312.24414, 1
                }
                name: string = "SLIME_DraftRacingGoal_Order2"
            }
            0xb0d8e7bb = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8367.15625, -35.4129333, 6931.32031, 1
                }
                name: string = "SLIME_DraftRacingGoal_Chaos3"
            }
            0x1be1cf92 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1816.98267, -46.0064392, 8408.50976, 1
                }
                name: string = "SLIME_BE_Order_Start3"
            }
            0x1f49b797 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    11186.9736, -30.893219, 5409.39404, 1
                }
                name: string = "SLIME_BR_Chaos_Inner"
            }
            0x80f125cc = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    10937.501, -33.2415771, 6119.39746, 1
                }
                name: string = "SLIME_TurretFacing_RI_BOT"
            }
            0x32c78506 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    2628.59399, -30.8940735, 7676.68115, 1
                }
                name: string = "SLIME_NexusBlitz_SpawnBlue"
            }
            0xbd758f56 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7024.71973, -46.0037537, 8170.68213, 1
                }
                name: string = "SLIME_BE_Order_End4"
            }
            0x06f52655 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7638.90625, -35.4180603, 3295.44531, 1
                }
                name: string = "SLIME_BR_Neutral_Bot"
            }
            0xdd447e82 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9078.30371, -58.539032, 9723.12305, 1
                }
                name: string = "SLIME_BR_Chaos_Jungle_UpperTower"
            }
            0x9bbeede4 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    9602.53027, -30.893219, 4858.83789, 1
                }
                name: string = "SLIME_BR_Chaos_Lower_Outer"
            }
            0xa45db1bc = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    6771.95508, -30.8944397, 6965.20361, 1
                }
                name: string = "SLIME_BR_Order_Upper_Outer"
            }
            0x7feece71 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    6167.67432, -41.477478, 3723.43896, 1
                }
                name: string = "SLIME_TurretFacing_LO_BOT"
            }
            0xade8ac7d = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9749.50488, -35.4183044, 4685.20117, 1
                }
                name: string = "SLIME_DraftRacingGoal_Chaos1"
            }
            0x1b38b0ab = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999969602, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969602, 0
                    751.704468, 32.1994324, 4144.11914, 1
                }
                name: string = "SLIME_EnvMinion"
            }
            0xcf7dec2b = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2047.3125, -46.0053406, 7827.375, 1
                }
                name: string = "SLIME_KingPoroOrder"
            }
            0x89a425b0 = MapLocator {
                0xad304db5: string = "Characters/URF_FeeneyPult/Skins/Skin1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.445980608, -0.00515315775, 0.895027816, 0
                    0.00505142007, 0.999953032, 0.00827432517, 0
                    -0.895028412, 0.00821134914, -0.44593364, 0
                    14034.4482, -41.4780006, 8811.31348, 1
                }
                name: string = "SLIME_FeeneypultChaos"
            }
            0x93381c37 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    12695.1738, -63.8010712, 7211.53223, 1
                }
                name: string = "SLIME_TurretFacing_RN_BOT"
            }
            0xcf2387be = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1764.79761, -46.0048523, 9260.98926, 1
                }
                name: string = "SLIME_BE_Order_Start1"
            }
            0x4e6a197d = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Yellow"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7570, -5, 5392.58008, 1
                }
                name: string = "SLIME_ScuttleTrackCenter"
            }
            0x6e6a879a = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5435.47558, -46.000824, 7705.82373, 1
                }
                name: string = "SLIME_BE_Order_Start2"
            }
            0xa67964d1 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7592.78613, -35.4205017, 9152.01758, 1
                }
                name: string = "SLIME_BR_Neutral_RH"
            }
            0x51a1e8c0 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Yellow"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7820, 0, 7698.79102, 1
                }
                name: string = "SLIME_ScuttleStart2"
            }
            0x7eb35ee3 = GdsMapObject {
                boxMin: vec3 = { 1962.3103, -41.4743042, 7916.95508 }
                boxMax: vec3 = { 2056.93237, 242.251587, 8011.57715 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    2100.62109, -41.473999, 7964.26611, 1
                }
                name: string = "__P_Order_Spawn_Barracks__L01"
            }
            0xa99c3cce = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3291.75976, -46.0027771, 6787.27686, 1
                }
                name: string = "SLIME_BE_Order_Start5"
            }
            0x1fed4741 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8159.81738, -46.0018005, 8127.30908, 1
                }
                name: string = "SLIME_BE_Chaos_End4"
            }
            0xb4727475 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8831.34961, -46.0037537, 5214.36328, 1
                }
                name: string = "SLIME_BE_Chaos_Start4"
            }
            0x5d5f1c93 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7582.86377, -35.4205017, 6500.42529, 1
                }
                name: string = "SLIME_BR_Neutral_BlueBuff"
            }
            0x0f9da845 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    6213.87939, -41.4777222, 6850.54394, 1
                }
                name: string = "SLIME_TurretFacing_LO"
            }
            0x813cafdc = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    6047.40723, -30.8946838, 5755.00293, 1
                }
                name: string = "SLIME_BR_Order_Upper_Raptors"
            }
            0x7c05342c = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8350.42285, -35.4170837, 9377.41211, 1
                }
                name: string = "SLIME_BR_Neutral_RightPassage"
            }
            0xf399141a = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    12661.6816, -30.8939514, 7634.86768, 1
                }
                name: string = "SLIME_NexusBlitz_SpawnRed"
            }
            0xd8bc10b3 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7078.6543, -46.0018005, 6366.98096, 1
                }
                name: string = "SLIME_BE_Order_End6"
            }
            0x26019380 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7608.60254, -35.4201355, 10183.0098, 1
                }
                name: string = "SLIME_BR_Neutral_RedBuff"
            }
            0x610ba039 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10723.082, -35.4205017, 8456.79492, 1
                }
                name: string = "SLIME_BR_Chaos_Jungle_Tower"
            }
            0x58a505a0 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    8438.10742, -30.8929749, 3692.37842, 1
                }
                name: string = "SLIME_BR_Chaos_Lower_Outer_South"
            }
            0x80ed8d7a = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    7608.35352, -30.8935852, 7022.31592, 1
                }
                name: string = "SLIME_NexusBlitz_EndPoint"
            }
            0xe64c8f93 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6108.47803, -46.0027771, 4484.99463, 1
                }
                name: string = "SLIME_BE_Order_Start6"
            }
            0x8d9af3b8 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    6139.84473, -30.8937073, 9724.79492, 1
                }
                name: string = "SLIME_BR_Order_Jungle_UpperTower"
            }
            0x2cd4b85c = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    8520.43555, -41.4738159, 9750.62305, 1
                }
                name: string = "LootGoblinHeraldPitRight"
            }
            0xded7a619 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    13248.0537, -46.0066223, 8690.0625, 1
                }
                name: string = "SLIME_BE_Chaos_Start1"
            }
            0x061e9ed2 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9675.8125, -46.0022888, 5111.00684, 1
                }
                name: string = "SLIME_BE_Chaos_End3"
            }
            0x09ab1b62 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    5474.44531, -41.4744263, 8755.28516, 1
                }
                name: string = "SLIME_TurretFacing_LJ"
            }
            0x15fd1647 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    7598.89258, -41.475769, 5463.99805, 1
                }
                name: string = "SLIME_Map_MidPoint"
            }
            0x85df3f89 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    10115.6855, -41.4760017, 4180.27881, 1
                }
                name: string = "LootGoblinBotLaneRight"
            }
            0xc958ebc4 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    5449.59277, -30.893219, 4854.17139, 1
                }
                name: string = "SLIME_BR_Order_Lower_Outer"
            }
            0x6b68e833 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7643.96826, -35.4180984, 3423.51855, 1
                }
                name: string = "SLIME_BR_Neutral_Bot_GoblinFriendly"
            }
            0xb7fec5e5 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7055.97852, -35.4195251, 3837.88184, 1
                }
                name: string = "SLIME_BR_Neutral_Bot1"
            }
            0xc4e72bfb = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    4308.15039, -30.8917542, 8201.85547, 1
                }
                name: string = "SLIME_BR_Order_Jungle_Tower"
            }
            0x33b845fe = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    13227.54, -46.0027161, 8595.11133, 1
                }
                name: string = "SLIME_BE_Chaos_Start6"
            }
            0x4681b569 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    9274.7002, -30.8946838, 5695.0835, 1
                }
                name: string = "SLIME_BR_Chaos_Upper_Outer_Raptors"
            }
            0x6f9e5fa3 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    10282.6533, -41.4730835, 6604.42236, 1
                }
                name: string = "LootGoblinRightEdge"
            }
            0x41172d73 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7601.56836, -39.6717224, 3753.41894, 1
                }
                name: string = "SLIME_PushCartCenterLocator2"
            }
            0x30f832f1 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    9023.46973, -41.4777222, 3698.9541, 1
                }
                name: string = "SLIME_TurretFacing_RO_BOT"
            }
            0xd404f40e = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7584.70264, -35.4197693, 3947.83398, 1
                }
                name: string = "SLIME_BR_Neutral_FightCase"
            }
            0x71c8f90e = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    3788.25122, -30.8944397, 5549.81396, 1
                }
                name: string = "SLIME_BR_Order_Inner"
            }
            0x854c326c = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8171.25684, -35.4187927, 6465.15771, 1
                }
                name: string = "SLIME_BR_Neutral_RightCase"
            }
            0xb0d63e34 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6344.58936, -35.4151306, 9055.87695, 1
                }
                name: string = "SLIME_BR_Neutral_LeftIsland"
            }
            0x9fcbdbfa = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6900.29932, -35.4163513, 6993.18115, 1
                }
                name: string = "SLIME_DraftRacingGoal_Order3"
            }
            0xff19e611 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    8460.40234, -30.8941956, 6945.03516, 1
                }
                name: string = "SLIME_BR_Chaos_Upper_Outer"
            }
            0x38b10115 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Yellow"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7320, 0, 7698.79102, 1
                }
                name: string = "SLIME_ScuttleStart1"
            }
            0x6541e810 = GdsMapObject {
                boxMin: vec3 = { 13067.373, -41.4776001, 7823.53418 }
                boxMax: vec3 = { 13161.9961, 242.248291, 7918.15625 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    13039.3789, -41.4780006, 7964.26611, 1
                }
                name: string = "__P_Chaos_Spawn_Barracks__L01"
            }
            0xe849f3f1 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6385.25586, -46.0013123, 5181.60986, 1
                }
                name: string = "SLIME_BE_Order_Start4"
            }
            0xfdb899bf = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10187.5869, -46.0052185, 7774.35498, 1
                }
                name: string = "SLIME_BE_Chaos_End1"
            }
            0x2d061215 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7897.55469, -46.0035095, 5151.1958, 1
                }
                name: string = "SLIME_BE_Chaos_End2"
            }
            0x593fed6d = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    2697.2146, -41.4772339, 8031.07617, 1
                }
                name: string = "SLIME_TurretFacing_LN"
            }
            0xfc5459da = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    1736.16248, 32.1990013, 9211.57031, 1
                }
                name: string = "SLIME_FountainLocator_Left1"
            }
            0x655ea684 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    1936.91174, 32.1990013, 8766.48926, 1
                }
                name: string = "NEXUSBLITZ_OrderBarrierFacePos"
            }
            0x5c9bbde3 = MapLocator {
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    13300.21, 32.1987572, 8807.42383, 1
                }
                name: string = "NEXUSBLITZ_ChaosBarrierFacePos"
            }
            0xd433a6e4 = MapLocator {
                0xad304db5: string = "Characters/SLIME_Warthog/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.929374993, 0.00506172702, -0.369107485, 0
                    0.00169778126, 0.999954045, 0.00943795219, 0
                    0.36913833, 0.00814472884, -0.929340839, 0
                    1484.2627, 25.7223358, 8925.11621, 1
                }
                name: string = "NB_OrderBattleSled"
            }
            0xc527f0ba = MapLocator {
                0xad304db5: string = "Characters/SLIME_Warthog/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.940036118, -0.00515163923, 0.341035903, 0
                    -0.00204561232, 0.999953032, 0.00946659222, 0
                    -0.341068655, 0.00820131227, -0.940002501, 0
                    13765.7373, 25.7220001, 8925.11621, 1
                }
                name: string = "NB_ChaosBattleSled"
            }
        }
        path: string = "Maps/MapGeometry/Map21/Chunks/Locators"
    }
    "Maps/MapGeometry/Map21/Chunks/MapObjects" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x30a2a88d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10516.1602, -86.094635, 4286.5083 }
                boxMax: vec3 = { 10681.206, 74.2316208, 4441.2627 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.839360774, 0.0829185396, -0.228908449, 0
                    -0.105344854, 0.994090974, -0.0261841211, 0
                    0.225384682, 0.0460922457, 0.843136013, 0
                    10606.2852, -77.6692047, 4365.7749, 1
                }
                name: string = "LevelProp_brush_SRU_G33"
            }
            0xd33c2c71 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8579.13086, -46.3125916, 3068.32153 }
                boxMax: vec3 = { 8763.49414, 167.293304, 3252.6853 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8671.3125, -46.3125916, 3160.50342, 1
                }
                name: string = "LevelProp_brush_SRU_A20"
            }
            0x5e6ae9ef = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8046.0752, -33.8023453, 8071.11133 }
                boxMax: vec3 = { 8256.40527, 179.977386, 8281.44141 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.859185994, 0, -0.160011321, 0
                    0, 1, 0, 0
                    0.160011321, 0, 0.859185994, 0
                    8151.24023, -33.6285019, 8176.27637, 1
                }
                name: string = "LevelProp_brush_SRU_I30"
            }
            0x2dedaee6 = GdsMapObject {
                type: u8 = 5
                boxMin: vec3 = { 9236.83984, -21.0082741, 6558.57959 }
                boxMax: vec3 = { 9652.24414, 652.120056, 6973.98486 }
                0xad304db5: string = "Characters/SRUAP_Turret_Chaos1/Skins/Skin10"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    -0.719339669, -6.28866772e-08, 0.694658399, 0
                    -1.48151727e-07, 0.999999881, -6.28866772e-08, 0
                    -0.694658279, -1.48151727e-07, -0.719339669, 0
                    9444.54199, -8, 6766.28223, 1
                }
                name: string = "Turret_T2_C_04"
            }
            0xe0034d63 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9578.01953, -46.3129196, 9965.73926 }
                boxMax: vec3 = { 9742.45703, 131.079773, 10130.1768 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    9660.23828, -46.3129196, 10047.958, 1
                }
                name: string = "LevelProp_brush_SRU_D24"
            }
            0x541f8368 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10596.4541, -46.4091644, 4244.05176 }
                boxMax: vec3 = { 10806.7568, 135.868851, 4454.35449 }
                0xad304db5: string = "Characters/brush_SRU_E/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    10701.6055, -46.3116455, 4349.20312, 1
                }
                name: string = "LevelProp_brush_SRU_E10"
            }
            0x31ac4915 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10591.0752, -77.0042419, 4131.70752 }
                boxMax: vec3 = { 10758.6943, 65.9943085, 4299.32471 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    10674.8848, -77.6690826, 4215.51611, 1
                }
                name: string = "LevelProp_brush_SRU_G32"
            }
            0x41f92a5f = GdsMapObject {
                type: u8 = 5
                boxMin: vec3 = { 5459.82373, -24.8579884, 6505.8418 }
                boxMax: vec3 = { 6024.95703, 693.858093, 7067.34668 }
                0xad304db5: string = "Characters/SRUAP_Turret_Chaos1/Skins/Skin11"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.707106769, 0, -0.707106769, 0
                    0, 1, 0, 0
                    0.707106769, 0, 0.707106769, 0
                    5762.98096, -8, 6805.35205, 1
                }
                name: string = "Turret_T1_C_04"
            }
            0xe5fbb9cc = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5401.92432, -43.1349258, 10050.7002 }
                boxMax: vec3 = { 5599.91943, 163.626953, 10248.6943 }
                0xad304db5: string = "Characters/brush_SRU_J/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    5500.92188, -42.9611588, 10149.6973, 1
                }
                name: string = "LevelProp_brush_SRU_J3"
            }
            0x8e2db8bd = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 11087.8867, -48.0086517, 4550.19531 }
                boxMax: vec3 = { 11215.9434, 94.9898987, 4678.25098 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    11151.915, -48.6734924, 4614.22314, 1
                }
                name: string = "LevelProp_brush_SRU_G24"
            }
            0x0253af63 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7977.6123, -65.5800781, 4431.56396 }
                boxMax: vec3 = { 8230.31445, 148.199661, 4684.26611 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.528345287, 0, 0.696172476, 0
                    0, 1, 0, 0
                    -0.696172476, 0, 0.528345287, 0
                    8103.96338, -65.4062347, 4557.91504, 1
                }
                name: string = "LevelProp_brush_SRU_I7"
            }
            0x43567b65 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6975.97656, -65.5793152, 7873.12402 }
                boxMax: vec3 = { 7213.94434, 148.200424, 8111.0918 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.79900521, 0, 0.354113579, 0
                    0, 1, 0, 0
                    -0.354113579, 0, 0.79900521, 0
                    7094.96045, -65.4054718, 7992.10791, 1
                }
                name: string = "LevelProp_brush_SRU_I29"
            }
            0xcc09c4a0 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6259.76221, -46.4314728, 3088.28687 }
                boxMax: vec3 = { 6457.44092, 135.846542, 3285.96558 }
                0xad304db5: string = "Characters/brush_SRU_E/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.822188079, 0, 0.296327591, 0
                    0, 1, 0, 0
                    -0.296327591, 0, 0.822188079, 0
                    6358.60156, -46.3339539, 3187.12622, 1
                }
                name: string = "LevelProp_brush_SRU_E7"
            }
            0x67b8b0df = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9499.81445, -46.3118057, 4682.67383 }
                boxMax: vec3 = { 9707.88086, 131.080902, 4890.74219 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.655681968, 0, 0.5778265, 0
                    0, 1, 0, 0
                    -0.5778265, 0, 0.655681968, 0
                    9603.84766, -46.3118057, 4786.70801, 1
                }
                name: string = "LevelProp_brush_SRU_D6"
            }
            0x48eae403 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8317.5166, -48.0096588, 3128.82568 }
                boxMax: vec3 = { 8444.13379, 94.9888916, 3255.44189 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8380.8252, -48.6744995, 3192.13379, 1
                }
                name: string = "LevelProp_brush_SRU_G29"
            }
            0x483d0fc2 = GdsMapObject {
                type: u8 = 5
                boxMin: vec3 = { 9127.51758, -74.3292999, 3642.32226 }
                boxMax: vec3 = { 9607.28125, 635.648499, 4073.04736 }
                0xad304db5: string = "Characters/SRUAP_Turret_Chaos1/Skins/Skin10"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    -0.811673701, -0.0654483512, 0.580432951, 0
                    -0.0920789912, 0.995615065, -0.0164992828, 0
                    -0.576807916, -0.0668377131, -0.814140916, 0
                    9397.18945, -8, 3863.02197, 1
                }
                name: string = "Turret_T2_C_03"
            }
            0xf0ebf94b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5468.4375, -46.3125839, 10082.8418 }
                boxMax: vec3 = { 5691.77734, 167.293304, 10306.1816 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    5580.10742, -46.3125839, 10194.5117, 1
                }
                name: string = "LevelProp_brush_SRU_A8"
            }
            0x51afce36 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10362.4668, -46.3132248, 8285.38281 }
                boxMax: vec3 = { 10562.4141, 167.292664, 8485.33008 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    10462.4404, -46.3132248, 8385.35644, 1
                }
                name: string = "LevelProp_brush_SRU_A30"
            }
            0xaa001f70 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5725.13525, -82.9672394, 4743.26709 }
                boxMax: vec3 = { 5881.97314, 71.5572433, 4902.37451 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.843764842, 0.0241885763, -0.226443812, 0
                    -0.0446046665, 0.997220397, -0.0596814863, 0
                    0.224370778, 0.060457591, 0.842498362, 0
                    5806.77295, -77.6685333, 4827.12744, 1
                }
                name: string = "LevelProp_brush_SRU_G34"
            }
            0x861195ba = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6981.21387, -59.8543701, 8281.45312 }
                boxMax: vec3 = { 7113.71289, 83.1441803, 8413.95312 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    7047.46338, -60.5192108, 8347.70312, 1
                }
                name: string = "LevelProp_brush_SRU_G45"
            }
            0xa90264ba = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7334.88672, -49.1507797, 5903.53467 }
                boxMax: vec3 = { 7469.75391, 174.461243, 6038.40186 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873620808, 0, 0.0243072212, 0
                    0, 1, 0, 0
                    -0.0243072212, 0, 0.873620808, 0
                    7402.32031, -46.3113403, 5970.96826, 1
                }
                name: string = "LevelProp_brush_SRU_C2"
            }
            0x43e8a183 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5592.71924, -46.3122177, 10130.2168 }
                boxMax: vec3 = { 5776.39404, 131.080475, 10313.8926 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    5684.55664, -46.3122177, 10222.0547, 1
                }
                name: string = "LevelProp_brush_SRU_D7"
            }
            0x71a5d3e7 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9565.53808, -59.8565369, 10012.4072 }
                boxMax: vec3 = { 9702.85644, 83.1420135, 10149.7256 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    9634.19726, -60.5213776, 10081.0664, 1
                }
                name: string = "LevelProp_brush_SRU_G42"
            }
            0xbe76e0ff = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4078.53418, -46.3116455, 4401.1875 }
                boxMax: vec3 = { 4279.25391, 131.081055, 4601.90723 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    4178.89404, -46.3116455, 4501.54736, 1
                }
                name: string = "LevelProp_brush_SRU_D2"
            }
            0x16c394dd = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9351.19922, -46.3129807, 10050.3984 }
                boxMax: vec3 = { 9551.14648, 167.292908, 10250.3457 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    9451.17285, -46.3129807, 10150.3721, 1
                }
                name: string = "LevelProp_brush_SRU_A32"
            }
            0x21267333 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10449.0859, -46.6995201, 8239.16602 }
                boxMax: vec3 = { 10657.1562, 155.043365, 8447.23633 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    10553.1211, -46.31353, 8343.20117, 1
                }
                name: string = "LevelProp_brush_SRU_F23"
            }
            0x7434fe2f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5470.63672, -46.3105469, 4790.5249 }
                boxMax: vec3 = { 5671.35644, 131.082153, 4991.24463 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    5570.99658, -46.3105469, 4890.88476, 1
                }
                name: string = "LevelProp_brush_SRU_D20"
            }
            0x6755abe5 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4583.26172, -46.3117905, 8278.91894 }
                boxMax: vec3 = { 4766.93652, 131.080902, 8462.59473 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    4675.09912, -46.3117905, 8370.75684, 1
                }
                name: string = "LevelProp_brush_SRU_D27"
            }
            0xdef16fff = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10741.4375, -65.5802841, 4463.33984 }
                boxMax: vec3 = { 10929.0449, 148.199463, 4650.94629 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    10835.2412, -65.4064407, 4557.14307, 1
                }
                name: string = "LevelProp_brush_SRU_I13"
            }
            0xb1ec0216 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4224.98682, 22.6290951, 4268.12451 }
                boxMax: vec3 = { 4403.71338, 246.241119, 4446.85107 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    4314.3501, 25.4685364, 4357.48779, 1
                }
                name: string = "LevelProp_brush_SRU_C3"
            }
            0x70c034b2 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5607.5581, -46.4322281, 10010.2129 }
                boxMax: vec3 = { 5800.00244, 135.845795, 10202.6562 }
                0xad304db5: string = "Characters/brush_SRU_E/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    5703.78027, -46.3347092, 10106.4346, 1
                }
                name: string = "LevelProp_brush_SRU_E4"
            }
            0x25d26d84 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 7071.40967, -43.7530823, 3613.93726 }
                boxMax: vec3 = { 7166.03174, 239.972809, 3708.55933 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    7118.72119, -43.7529984, 3533.81201, 1
                }
                name: string = "__NAV_R006"
            }
            0x97173b8a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8681.08594, -65.5811691, 3015.80347 }
                boxMax: vec3 = { 8866.58398, 148.198578, 3201.30151 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8773.83496, -65.4073257, 3108.55249, 1
                }
                name: string = "LevelProp_brush_SRU_I15"
            }
            0x3bf075dd = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4476.00342, -44.3143539, 4173.55566 }
                boxMax: vec3 = { 4613.64404, 179.297668, 4311.19629 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    4544.82373, -41.4749146, 4242.37598, 1
                }
                name: string = "LevelProp_brush_SRU_C74"
            }
            0x74d10bd1 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 8378.4834, -41.4772339, 6753.6875 }
                boxMax: vec3 = { 8473.10644, 242.248657, 6848.30957 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    8425.79492, -41.4770012, 6700, 1
                }
                name: string = "__NAV_L005"
            }
            0x637503df = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10312.9805, -59.8564148, 8438.19922 }
                boxMax: vec3 = { 10450.2988, 83.1421356, 8575.51758 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    10381.6396, -60.5212555, 8506.8584, 1
                }
                name: string = "LevelProp_brush_SRU_G40"
            }
            0x2e7d0a42 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10534.8066, -46.3112793, 4204.16357 }
                boxMax: vec3 = { 10735.5254, 131.081421, 4404.8833 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    10635.166, -46.3112793, 4304.52344, 1
                }
                name: string = "LevelProp_brush_SRU_D16"
            }
            0x6566eed0 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4217.12695, -46.3117676, 4405.59717 }
                boxMax: vec3 = { 4429.11328, 182.933136, 4617.5835 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    4323.12012, -46.3117676, 4511.59033, 1
                }
                name: string = "LevelProp_brush_SRU_B5"
            }
            0x9606313e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6890.34082, -43.1332626, 8195.45508 }
                boxMax: vec3 = { 7100.01367, 163.628601, 8405.12695 }
                0xad304db5: string = "Characters/brush_SRU_J/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.79900521, 0, 0.354113579, 0
                    0, 1, 0, 0
                    -0.354113579, 0, 0.79900521, 0
                    6995.17725, -42.9594955, 8300.29102, 1
                }
                name: string = "LevelProp_brush_SRU_J17"
            }
            0xa811e811 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8150.31885, -46.3108673, 8057.92969 }
                boxMax: vec3 = { 8350.89258, 167.295029, 8258.50391 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.866878152, 0, -0.11102581, 0
                    0, 1, 0, 0
                    0.11102581, 0, 0.866878152, 0
                    8250.60547, -46.3108673, 8158.2168, 1
                }
                name: string = "LevelProp_brush_SRU_A37"
            }
            0x833ff0b7 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8362.75488, -48.0097809, 3118.74829 }
                boxMax: vec3 = { 8489.37207, 94.9887695, 3245.3645 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8426.06348, -48.6746216, 3182.0564, 1
                }
                name: string = "LevelProp_brush_SRU_G27"
            }
            0x67f98825 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6931.27441, -46.3111801, 8114.5249 }
                boxMax: vec3 = { 7124.20312, 167.294708, 8307.45312 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    7027.73877, -46.3111801, 8210.98926, 1
                }
                name: string = "LevelProp_brush_SRU_A33"
            }
            0x5ca026de = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8024.82764, -46.3114548, 8199.9043 }
                boxMax: vec3 = { 8233.87109, 167.294434, 8408.94726 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.859185994, 0, -0.160011321, 0
                    0, 1, 0, 0
                    0.160011321, 0, 0.859185994, 0
                    8129.34961, -46.3114548, 8304.42578, 1
                }
                name: string = "LevelProp_brush_SRU_A38"
            }
            0x24b2a292 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9483.64062, -46.3132248, 10055.1797 }
                boxMax: vec3 = { 9657.30859, 182.931671, 10228.8476 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    9570.47461, -46.3132248, 10142.0137, 1
                }
                name: string = "LevelProp_brush_SRU_B23"
            }
            0x69818b1b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9408.62695, -41.8654213, 4578.21728 }
                boxMax: vec3 = { 9604.21875, 159.877457, 4773.81104 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    9506.42285, -41.4794312, 4676.01416, 1
                }
                name: string = "LevelProp_brush_SRU_F10"
            }
            0x3bbee5ef = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10848.9473, -46.3116455, 4506.20557 }
                boxMax: vec3 = { 11010.8984, 182.933258, 4668.15771 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    10929.9228, -46.3116455, 4587.18164, 1
                }
                name: string = "LevelProp_brush_SRU_B17"
            }
            0x0098e331 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10818.4805, -46.6976357, 4486.604 }
                boxMax: vec3 = { 11012.5137, 155.045242, 4680.63721 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    10915.4971, -46.3116455, 4583.6206, 1
                }
                name: string = "LevelProp_brush_SRU_F18"
            }
            0x6f8eb0f6 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6897.95312, -46.6969109, 8079.70361 }
                boxMax: vec3 = { 7144.07226, 155.045959, 8325.82226 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.79900521, 0, 0.354113579, 0
                    0, 1, 0, 0
                    -0.354113579, 0, 0.79900521, 0
                    7021.0127, -46.3109207, 8202.7627, 1
                }
                name: string = "LevelProp_brush_SRU_F32"
            }
            0x72acbca8 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4662.5498, -48.0095901, 8384.9707 }
                boxMax: vec3 = { 4815.93359, 94.9889603, 8538.35547 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    4739.2417, -48.6744308, 8461.66308, 1
                }
                name: string = "LevelProp_brush_SRU_G9"
            }
            0xdbf87bac = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4134.63818, -46.6978188, 4337.45654 }
                boxMax: vec3 = { 4388.6167, 155.045059, 4591.43506 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    4261.62744, -46.3118286, 4464.4458, 1
                }
                name: string = "LevelProp_brush_SRU_F4"
            }
            0x236c609a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4111.50146, -46.3117676, 4463.4668 }
                boxMax: vec3 = { 4323.48779, 182.933136, 4675.45312 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    4217.49463, -46.3117676, 4569.45996, 1
                }
                name: string = "LevelProp_brush_SRU_B1"
            }
            0xf51b0765 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8752.6709, -46.3127136, 2936.99438 }
                boxMax: vec3 = { 8912.80371, 182.93219, 3097.12573 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8832.7373, -46.3127136, 3017.06006, 1
                }
                name: string = "LevelProp_brush_SRU_B18"
            }
            0x8d518480 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 3966.89941, -65.5804062, 4510.43213 }
                boxMax: vec3 = { 4212.46631, 148.199341, 4755.99854 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    4089.6831, -65.4065628, 4633.21533, 1
                }
                name: string = "LevelProp_brush_SRU_I1"
            }
            0x0efed025 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9474.01367, -46.6990929, 9943.58008 }
                boxMax: vec3 = { 9682.08398, 155.043793, 10151.6504 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    9578.04883, -46.3131027, 10047.6152, 1
                }
                name: string = "LevelProp_brush_SRU_F24"
            }
            0x4c2dbea6 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4340.47363, -43.1342316, 4439.45801 }
                boxMax: vec3 = { 4556.8418, 163.62764, 4655.82617 }
                0xad304db5: string = "Characters/brush_SRU_J/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    4448.65771, -42.9604645, 4547.64209, 1
                }
                name: string = "LevelProp_brush_SRU_J1"
            }
            0x55d18ff0 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6686.82178, -46.6974525, 2967.71704 }
                boxMax: vec3 = { 6942.12256, 155.045425, 3223.01733 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.442454994, 0, 0.753682196, 0
                    0, 1, 0, 0
                    -0.753682196, 0, 0.442454994, 0
                    6814.47217, -46.3114624, 3095.36719, 1
                }
                name: string = "LevelProp_brush_SRU_F15"
            }
            0xc409e56f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5603.396, -59.8557739, 9998.22949 }
                boxMax: vec3 = { 5756.77978, 83.1427765, 10151.6142 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    5680.08789, -60.5206146, 10074.9219, 1
                }
                name: string = "LevelProp_brush_SRU_G37"
            }
            0x66245311 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4528.76367, -95.0764313, 4179.47217 }
                boxMax: vec3 = { 4696.38086, 47.9221191, 4347.08936 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    4612.57226, -95.741272, 4263.28076, 1
                }
                name: string = "LevelProp_brush_SRU_G4"
            }
            0xd697fb32 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9433.29394, -46.3119278, 4887.3374 }
                boxMax: vec3 = { 9686.29394, 167.293976, 5140.3374 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.655681968, 0, 0.5778265, 0
                    0, 1, 0, 0
                    -0.5778265, 0, 0.655681968, 0
                    9559.79394, -46.3119278, 5013.8374, 1
                }
                name: string = "LevelProp_brush_SRU_A4"
            }
            0xe5a4d482 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9561.56543, -65.5805054, 4814.88476 }
                boxMax: vec3 = { 9816.12402, 148.199234, 5069.44238 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.655681968, 0, 0.5778265, 0
                    0, 1, 0, 0
                    -0.5778265, 0, 0.655681968, 0
                    9688.84473, -65.406662, 4942.16357, 1
                }
                name: string = "LevelProp_brush_SRU_I4"
            }
            0xf7ce6e29 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7046.85596, -65.5806732, 9280.4707 }
                boxMax: vec3 = { 7271.5708, 148.199066, 9505.18359 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    7159.21338, -65.4068298, 9392.82715, 1
                }
                name: string = "LevelProp_brush_SRU_I23"
            }
            0x06a9bfac = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9600.39551, -41.4790649, 4798.87256 }
                boxMax: vec3 = { 9788.35449, 172.126831, 4986.83154 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    9694.375, -41.4790649, 4892.85205, 1
                }
                name: string = "LevelProp_brush_SRU_A26"
            }
            0x4a13bc96 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4599.54639, -46.3122177, 8334.49121 }
                boxMax: vec3 = { 4822.88623, 167.293671, 8557.83105 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    4711.21631, -46.3122177, 8446.16113, 1
                }
                name: string = "LevelProp_brush_SRU_A15"
            }
            0x3a004c76 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8145.05127, -46.3108673, 8085.78174 }
                boxMax: vec3 = { 8345.625, 167.295029, 8286.35547 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.866878152, 0, -0.11102581, 0
                    0, 1, 0, 0
                    0.11102581, 0, 0.866878152, 0
                    8245.33789, -46.3108673, 8186.06885, 1
                }
                name: string = "LevelProp_brush_SRU_A36"
            }
            0xecc89182 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10296.792, -49.1521759, 8417.86426 }
                boxMax: vec3 = { 10443.2119, 174.459839, 8564.28418 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    10370.002, -46.3127365, 8491.07422, 1
                }
                name: string = "LevelProp_brush_SRU_C16"
            }
            0x273c0771 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6880.41699, -43.7541809, 9384.72266 }
                boxMax: vec3 = { 7034.99414, 133.638519, 9539.30078 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872872114, 0, 0.0435257256, 0
                    0, 1, 0, 0
                    -0.0435257256, 0, 0.872872114, 0
                    6957.70557, -43.7541809, 9462.01172, 1
                }
                name: string = "LevelProp_brush_SRU_D8"
            }
            0x38925597 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10484.5439, -43.1357498, 8257.31445 }
                boxMax: vec3 = { 10661.8018, 163.626129, 8434.57226 }
                0xad304db5: string = "Characters/brush_SRU_J/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    10573.1728, -42.9619827, 8345.94336, 1
                }
                name: string = "LevelProp_brush_SRU_J13"
            }
            0xea117951 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9260.18555, -46.3119278, 4712.04248 }
                boxMax: vec3 = { 9513.18555, 167.293976, 4965.04248 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.655681968, 0, 0.5778265, 0
                    0, 1, 0, 0
                    -0.5778265, 0, 0.655681968, 0
                    9386.68555, -46.3119278, 4838.54248, 1
                }
                name: string = "LevelProp_brush_SRU_A5"
            }
            0x8f840224 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6968.73633, -59.8557739, 9456.69531 }
                boxMax: vec3 = { 7122.12012, 83.1427765, 9610.08008 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    7045.42822, -60.5206146, 9533.3877, 1
                }
                name: string = "LevelProp_brush_SRU_G48"
            }
            0xf4ad9646 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4451.09131, -46.3115234, 4085.39795 }
                boxMax: vec3 = { 4651.81104, 131.081177, 4286.11768 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    4551.45117, -46.3115234, 4185.75781, 1
                }
                name: string = "LevelProp_brush_SRU_D3"
            }
            0x52e401c4 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7949.15527, -46.3114548, 8181.22754 }
                boxMax: vec3 = { 8130.72363, 182.933441, 8362.7959 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.859185994, 0, -0.160011321, 0
                    0, 1, 0, 0
                    0.160011321, 0, 0.859185994, 0
                    8039.93945, -46.3114548, 8272.01172, 1
                }
                name: string = "LevelProp_brush_SRU_B33"
            }
            0x0841feb9 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 13142.4521, -33.4295959, 7400.86475 }
                boxMax: vec3 = { 13237.0752, 250.296295, 7495.48682 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    13489.7637, -33.4300003, 7448.17578, 1
                }
                name: string = "__NAV_R012"
            }
            0xbc32d4b4 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6896.64111, -41.4779663, 9270.45898 }
                boxMax: vec3 = { 7059.89502, 187.766937, 9433.71289 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    6978.26807, -41.4779663, 9352.08594, 1
                }
                name: string = "LevelProp_brush_SRU_B9"
            }
            0x6655f1ab = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9575.21191, -46.3116837, 4974.44238 }
                boxMax: vec3 = { 9783.27832, 131.081024, 5182.51074 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.655681968, 0, 0.5778265, 0
                    0, 1, 0, 0
                    -0.5778265, 0, 0.655681968, 0
                    9679.24512, -46.3116837, 5078.47656, 1
                }
                name: string = "LevelProp_brush_SRU_D5"
            }
            0x161dd6dc = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4389.81885, -21.1405411, 4176.08398 }
                boxMax: vec3 = { 4544.396, 156.252167, 4330.66113 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    4467.10742, -21.1405411, 4253.37256, 1
                }
                name: string = "LevelProp_brush_SRU_D192"
            }
            0xf1fbcb34 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10994.5146, -46.3116455, 4538.73242 }
                boxMax: vec3 = { 11156.4658, 182.933258, 4700.68457 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    11075.4902, -46.3116455, 4619.7085, 1
                }
                name: string = "LevelProp_brush_SRU_B15"
            }
            0x9cbf0081 = GdsMapObject {
                type: u8 = 6
                boxMin: vec3 = { 2153.29077, 19.3945656, 8959.7168 }
                boxMax: vec3 = { 2686.72437, 411.430939, 9493.15039 }
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Shop_Blue"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    3.42989588, 0, -0.0267592911, 0
                    0, 3.43000007, 0, 0
                    0.0267592911, 0, 3.42989588, 0
                    2420.00757, -28.7299767, 9226.43359, 1
                }
                name: string = "OrderShop1"
            }
            0x2627825a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4434.75049, -46.6982079, 8276.47754 }
                boxMax: vec3 = { 4667.16162, 155.044678, 8508.88965 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    4550.95605, -46.3122177, 8392.68359, 1
                }
                name: string = "LevelProp_brush_SRU_F8"
            }
            0xf3d2a0a8 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6924.02246, -94.4800415, 9367.79004 }
                boxMax: vec3 = { 7111.98144, 119.125854, 9555.74902 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    7018.00195, -94.4800415, 9461.76953, 1
                }
                name: string = "LevelProp_brush_SRU_A35"
            }
            0xcbc89e26 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4009.59106, -59.8549576, 4466.53467 }
                boxMax: vec3 = { 4177.2085, 83.1435928, 4634.15186 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    4093.3999, -60.5197983, 4550.34326, 1
                }
                name: string = "LevelProp_brush_SRU_G2"
            }
            0xa4d8b231 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6798.60205, -46.312645, 9276.96289 }
                boxMax: vec3 = { 6982.27686, 131.080048, 9460.63867 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    6890.43945, -46.312645, 9368.80078, 1
                }
                name: string = "LevelProp_brush_SRU_D28"
            }
            0xffee96c3 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7473.09424, -46.3108749, 5875.28808 }
                boxMax: vec3 = { 7640.66553, 182.934021, 6042.85938 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    7556.87988, -46.3108749, 5959.07373, 1
                }
                name: string = "LevelProp_brush_SRU_B11"
            }
            0x312a02f9 = GdsMapObject {
                type: u8 = 3
                boxMin: vec3 = { 11533.3467, -455.414886, 6301.61914 }
                boxMax: vec3 = { 11908.5225, 273.66391, 6676.79394 }
                0xad304db5: string = "Characters/SRUAP_OrderInhibitor/Skins/Skin11"
                sceneLayer: string = "Map Objects"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11720.9346, -35.4148865, 6489.20654, 1
                }
                name: string = "Barracks_T2_R1"
            }
            0xd42f8315 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7935.75, -46.4309273, 4462.27051 }
                boxMax: vec3 = { 8148.5498, 135.847092, 4675.07031 }
                0xad304db5: string = "Characters/brush_SRU_E/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.462554663, 0, 0.741517842, 0
                    0, 1, 0, 0
                    -0.741517842, 0, 0.462554663, 0
                    8042.1499, -46.3334084, 4568.67041, 1
                }
                name: string = "LevelProp_brush_SRU_E6"
            }
            0xf9042926 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9411.04297, -43.1342697, 4818.39209 }
                boxMax: vec3 = { 9635.33203, 163.627594, 5042.68213 }
                0xad304db5: string = "Characters/brush_SRU_J/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.655681968, 0, 0.5778265, 0
                    0, 1, 0, 0
                    -0.5778265, 0, 0.655681968, 0
                    9523.1875, -42.9605026, 4930.53711, 1
                }
                name: string = "LevelProp_brush_SRU_J2"
            }
            0x599885bc = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8142.25537, -49.1501732, 4496.3916 }
                boxMax: vec3 = { 8323.10449, 174.461853, 4677.24023 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.462554663, 0, 0.741517842, 0
                    0, 1, 0, 0
                    -0.741517842, 0, 0.462554663, 0
                    8232.67969, -46.3107338, 4586.81592, 1
                }
                name: string = "LevelProp_brush_SRU_C7"
            }
            0xf6212119 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4492.34033, -65.5807343, 8266.75 }
                boxMax: vec3 = { 4717.05518, 148.199005, 8491.46289 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    4604.69775, -65.4068909, 8379.10644, 1
                }
                name: string = "LevelProp_brush_SRU_I17"
            }
            0x14fe4a33 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10916.3994, -65.5799789, 4371.26367 }
                boxMax: vec3 = { 11104.0068, 148.199768, 4558.87012 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    11010.2031, -65.4061356, 4465.06689, 1
                }
                name: string = "LevelProp_brush_SRU_I14"
            }
            0x2cfe1f1a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8331.75098, -48.0082397, 7931.05713 }
                boxMax: vec3 = { 8469.49902, 94.9903107, 8068.80713 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.866878152, 0, -0.11102581, 0
                    0, 1, 0, 0
                    0.11102581, 0, 0.866878152, 0
                    8400.625, -48.6730804, 7999.93213, 1
                }
                name: string = "LevelProp_brush_SRU_G51"
            }
            0x6ddda168 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9282.10742, -46.6979179, 4635.98975 }
                boxMax: vec3 = { 9545.38476, 155.044952, 4899.26709 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.655681968, 0, 0.5778265, 0
                    0, 1, 0, 0
                    -0.5778265, 0, 0.655681968, 0
                    9413.74609, -46.3119278, 4767.62842, 1
                }
                name: string = "LevelProp_brush_SRU_F5"
            }
            0x71659f6e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 3926.03833, -48.0089569, 4614.22656 }
                boxMax: vec3 = { 4093.65601, 94.9895935, 4781.84375 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    4009.84717, -48.6737976, 4698.03516, 1
                }
                name: string = "LevelProp_brush_SRU_G1"
            }
            0x43873236 = GdsMapObject {
                type: u8 = 6
                boxMin: vec3 = { 12352.293, 53.5368538, 8868.87793 }
                boxMax: vec3 = { 12883.1348, 443.667603, 9399.71973 }
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Shop_Blue"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    3.41322875, 0, -0.026625013, 0
                    0, 3.41332722, 0, 0
                    0.026625013, 0, 3.41322875, 0
                    12617.7139, 5.64624023, 9134.29883, 1
                }
                name: string = "ChaosShop"
            }
            0x93156a69 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5546.31104, -66.1651688, 4838.97998 }
                boxMax: vec3 = { 5762.6792, 140.59671, 5055.34814 }
                0xad304db5: string = "Characters/brush_SRU_J/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    5654.49512, -65.9914017, 4947.16406, 1
                }
                name: string = "LevelProp_brush_SRU_J11"
            }
            0x5c7a98dc = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6701.76514, -48.0082855, 2951.54565 }
                boxMax: vec3 = { 6870.25537, 94.9902649, 3120.03589 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.442454994, 0, 0.753682196, 0
                    0, 1, 0, 0
                    -0.753682196, 0, 0.442454994, 0
                    6786.01025, -48.6731262, 3035.79077, 1
                }
                name: string = "LevelProp_brush_SRU_G21"
            }
            0x2f0f3449 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8654.68359, -46.3125916, 3099.87427 }
                boxMax: vec3 = { 8839.04688, 167.293304, 3284.23804 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8746.86523, -46.3125916, 3192.05615, 1
                }
                name: string = "LevelProp_brush_SRU_A19"
            }
            0x626b434c = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9385.33887, -59.8562927, 10173.2578 }
                boxMax: vec3 = { 9522.65723, 83.1422577, 10310.5762 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    9453.99805, -60.5211334, 10241.917, 1
                }
                name: string = "LevelProp_brush_SRU_G41"
            }
            0x55c58f42 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10566.1328, -46.6975136, 4329.67236 }
                boxMax: vec3 = { 10820.1113, 155.045364, 4583.65088 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    10693.1221, -46.3115234, 4456.66162, 1
                }
                name: string = "LevelProp_brush_SRU_F21"
            }
            0x25dd861e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8498.23438, -46.6987038, 3105.48486 }
                boxMax: vec3 = { 8690.08594, 155.044174, 3297.33691 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8594.16016, -46.3127136, 3201.41089, 1
                }
                name: string = "LevelProp_brush_SRU_F20"
            }
            0x1798a9fc = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6814.83838, -46.6974144, 7990.72363 }
                boxMax: vec3 = { 7015.604, 155.045471, 8191.48926 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    6915.22119, -46.3114243, 8091.10644, 1
                }
                name: string = "LevelProp_brush_SRU_F25"
            }
            0xe917c599 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 10786.5391, -41.4767456, 4980.30225 }
                boxMax: vec3 = { 10881.1621, 242.249146, 5074.92432 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    10833.8506, -41.4767456, 5027.61328, 1
                }
                name: string = "__NAV_R010"
            }
            0x2a575f52 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8134.46289, -41.4769287, 9386.66894 }
                boxMax: vec3 = { 8297.7168, 187.767975, 9549.92285 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    8216.08984, -41.4769287, 9468.2959, 1
                }
                name: string = "LevelProp_brush_SRU_B28"
            }
            0x06abd760 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6845.79541, -59.855835, 9181.59668 }
                boxMax: vec3 = { 6999.1792, 83.1427155, 9334.98144 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    6922.4873, -60.5206757, 9258.28906, 1
                }
                name: string = "LevelProp_brush_SRU_G47"
            }
            0x58299a84 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10930.2959, -43.1341095, 4519.48486 }
                boxMax: vec3 = { 11095.5967, 163.627762, 4684.78467 }
                0xad304db5: string = "Characters/brush_SRU_J/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    11012.9463, -42.9603424, 4602.13476, 1
                }
                name: string = "LevelProp_brush_SRU_J7"
            }
            0xc91875d6 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4544.31934, -46.6980858, 8304.19922 }
                boxMax: vec3 = { 4776.73047, 155.0448, 8536.61133 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    4660.5249, -46.3120956, 8420.40527, 1
                }
                name: string = "LevelProp_brush_SRU_F12"
            }
            0x6bbd62e8 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5621.73584, -46.696537, 4774.38281 }
                boxMax: vec3 = { 5875.71436, 155.046341, 5028.36133 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    5748.7251, -46.3105469, 4901.37207, 1
                }
                name: string = "LevelProp_brush_SRU_F22"
            }
            0x4f790077 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5497.48047, -46.3106079, 4697.40918 }
                boxMax: vec3 = { 5698.2002, 131.082092, 4898.12891 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    5597.84033, -46.3106079, 4797.76904, 1
                }
                name: string = "LevelProp_brush_SRU_D18"
            }
            0x3a96a900 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8142.021, -38.9917603, 9447.02734 }
                boxMax: vec3 = { 8296.59863, 138.40094, 9601.60547 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    8219.30957, -38.9917603, 9524.31641, 1
                }
                name: string = "LevelProp_brush_SRU_D34"
            }
            0xba691caf = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8149.86182, -46.6969795, 7931.69971 }
                boxMax: vec3 = { 8358.58301, 155.045898, 8140.42139 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.866878152, 0, -0.11102581, 0
                    0, 1, 0, 0
                    0.11102581, 0, 0.866878152, 0
                    8254.22266, -46.3109894, 8036.06055, 1
                }
                name: string = "LevelProp_brush_SRU_F27"
            }
            0xddde0706 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9379.12695, -46.3118057, 4743.5415 }
                boxMax: vec3 = { 9598.875, 182.933105, 4963.28857 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.655681968, 0, 0.5778265, 0
                    0, 1, 0, 0
                    -0.5778265, 0, 0.655681968, 0
                    9489.00098, -46.3118057, 4853.41504, 1
                }
                name: string = "LevelProp_brush_SRU_B6"
            }
            0xeb1b3d55 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10453.6016, -46.3133469, 8291.93359 }
                boxMax: vec3 = { 10627.2695, 182.931549, 8465.60156 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    10540.4355, -46.3133469, 8378.76758, 1
                }
                name: string = "LevelProp_brush_SRU_B22"
            }
            0x78270b44 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7410.09424, -59.8546524, 5936.82275 }
                boxMax: vec3 = { 7536.57764, 83.143898, 6063.30615 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873620808, 0, 0.0243072212, 0
                    0, 1, 0, 0
                    -0.0243072212, 0, 0.873620808, 0
                    7473.33594, -60.5194931, 6000.06445, 1
                }
                name: string = "LevelProp_brush_SRU_G12"
            }
            0x3b4ae0ed = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5434.56787, -19.6100864, 4701.02002 }
                boxMax: vec3 = { 5599.61377, 140.716171, 4855.77441 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.839360774, 0.0829185396, -0.228908449, 0
                    -0.105344854, 0.994090974, -0.0261841211, 0
                    0.225384682, 0.0460922457, 0.843136013, 0
                    5524.69287, -11.1846542, 4780.28662, 1
                }
                name: string = "LevelProp_brush_SRU_G35"
            }
            0xbb071b1d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6875.34424, -42.5159302, 9435.77539 }
                boxMax: vec3 = { 7029.92139, 134.87677, 9590.35352 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    6952.63281, -42.5159302, 9513.06445, 1
                }
                name: string = "LevelProp_brush_SRU_D119"
            }
            0x1a4298cb = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 4912.57617, -41.4721069, 4364.04639 }
                boxMax: vec3 = { 5007.19824, 242.253784, 4458.66846 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    4959.88721, -41.4721069, 4411.35742, 1
                }
                name: string = "__NAV_R004"
            }
            0xf8b4546a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9591.87695, -36.4961548, 4732.4668 }
                boxMax: vec3 = { 9746.45508, 140.896545, 4887.04394 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    9669.16602, -36.4961548, 4809.75537, 1
                }
                name: string = "LevelProp_brush_SRU_D237"
            }
            0xbae624fe = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8255.19726, -33.8017578, 7987.52148 }
                boxMax: vec3 = { 8457.00586, 179.977982, 8189.33008 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.866878152, 0, -0.11102581, 0
                    0, 1, 0, 0
                    0.11102581, 0, 0.866878152, 0
                    8356.10156, -33.6279144, 8088.42578, 1
                }
                name: string = "LevelProp_brush_SRU_I25"
            }
            0x4aaf3988 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10652.8945, -59.8545303, 4377.5581 }
                boxMax: vec3 = { 10780.9512, 83.1440201, 4505.61377 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    10716.9228, -60.519371, 4441.58594, 1
                }
                name: string = "LevelProp_brush_SRU_G25"
            }
            0x6ba9fa24 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6993.3374, -46.3107376, 8199.45312 }
                boxMax: vec3 = { 7198.76318, 182.934174, 8404.87891 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.79900521, 0, 0.354113579, 0
                    0, 1, 0, 0
                    -0.354113579, 0, 0.79900521, 0
                    7096.05029, -46.3107376, 8302.16602, 1
                }
                name: string = "LevelProp_brush_SRU_B32"
            }
            0xc2b53db0 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5668.27783, -48.0094681, 10088.3408 }
                boxMax: vec3 = { 5821.66162, 94.9890823, 10241.7256 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    5744.96973, -48.6743088, 10165.0332, 1
                }
                name: string = "LevelProp_brush_SRU_G8"
            }
            0xda3d7d48 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9401.08496, -65.5816803, 10086.543 }
                boxMax: vec3 = { 9602.2627, 148.198059, 10287.7207 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    9501.67383, -65.4078369, 10187.1318, 1
                }
                name: string = "LevelProp_brush_SRU_I20"
            }
            0x30c10623 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10682.2617, -49.1507187, 4422.64502 }
                boxMax: vec3 = { 10818.8047, 174.461304, 4559.18799 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    10750.5332, -46.3112793, 4490.9165, 1
                }
                name: string = "LevelProp_brush_SRU_C9"
            }
            0xd1c891b7 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7751.1709, -46.3108749, 5835.72266 }
                boxMax: vec3 = { 7918.74219, 182.934021, 6003.29394 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    7834.95654, -46.3108749, 5919.5083, 1
                }
                name: string = "LevelProp_brush_SRU_B12"
            }
            0xa90a832a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6736.81006, -65.5798798, 7970.5918 }
                boxMax: vec3 = { 6930.92627, 148.19986, 8164.70801 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    6833.86816, -65.4060364, 8067.6499, 1
                }
                name: string = "LevelProp_brush_SRU_I21"
            }
            0xf28067e0 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5558.85644, -46.408371, 4569.67822 }
                boxMax: vec3 = { 5769.15918, 135.869644, 4779.98096 }
                0xad304db5: string = "Characters/brush_SRU_E/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    5664.00781, -46.3108521, 4674.82959, 1
                }
                name: string = "LevelProp_brush_SRU_E12"
            }
            0x52a8e0b0 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9674.89648, -48.008934, 4982.06787 }
                boxMax: vec3 = { 9848.65234, 94.9896164, 5155.82178 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.655681968, 0, 0.5778265, 0
                    0, 1, 0, 0
                    -0.5778265, 0, 0.655681968, 0
                    9761.77441, -48.6737747, 5068.94482, 1
                }
                name: string = "LevelProp_brush_SRU_G7"
            }
            0x7397c654 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5536.66357, -46.3106079, 4697.05957 }
                boxMax: vec3 = { 5780.72803, 167.295288, 4941.12402 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    5658.6958, -46.3106079, 4819.0918, 1
                }
                name: string = "LevelProp_brush_SRU_A28"
            }
            0xb5a83c75 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6784.34668, -59.8560791, 9385.80371 }
                boxMax: vec3 = { 6937.73047, 83.1424713, 9539.18848 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    6861.03857, -60.5209198, 9462.49609, 1
                }
                name: string = "LevelProp_brush_SRU_G44"
            }
            0x67bdd7a2 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 12830.5889, -41.4782104, 7735.44238 }
                boxMax: vec3 = { 12925.2119, 242.247681, 7830.06445 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    12977.9004, -41.4780006, 7633.33984, 1
                }
                name: string = "__NAV_L008"
            }
            0x8c6bec60 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4484.74707, -46.3123398, 8330.53516 }
                boxMax: vec3 = { 4708.08691, 167.293549, 8553.875 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    4596.41699, -46.3123398, 8442.20508, 1
                }
                name: string = "LevelProp_brush_SRU_A7"
            }
            0xa7896380 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4366.2627, -46.6976357, 4185.48047 }
                boxMax: vec3 = { 4620.24121, 155.045242, 4439.45898 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    4493.25195, -46.3116455, 4312.46973, 1
                }
                name: string = "LevelProp_brush_SRU_F2"
            }
            0xa7a4ab13 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5438.24219, -46.3104858, 4864.12305 }
                boxMax: vec3 = { 5650.22852, 182.934418, 5076.10938 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    5544.23535, -46.3104858, 4970.11621, 1
                }
                name: string = "LevelProp_brush_SRU_B20"
            }
            0xf3c6d208 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8058.65674, -59.8548584, 9466.79004 }
                boxMax: vec3 = { 8212.04102, 83.143692, 9620.1748 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    8135.34863, -60.5196991, 9543.48242, 1
                }
                name: string = "LevelProp_brush_SRU_G54"
            }
            0x0aca827b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10598.3496, -46.3118896, 4087.62378 }
                boxMax: vec3 = { 10784.8086, 167.294006, 4274.0835 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    10691.5791, -46.3118896, 4180.85352, 1
                }
                name: string = "LevelProp_brush_SRU_A16"
            }
            0xb85666a1 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7009.45947, -46.430809, 8128.52832 }
                boxMax: vec3 = { 7213.25439, 135.847198, 8332.32324 }
                0xad304db5: string = "Characters/brush_SRU_E/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.79900521, 0, 0.354113579, 0
                    0, 1, 0, 0
                    -0.354113579, 0, 0.79900521, 0
                    7111.35693, -46.3332901, 8230.42578, 1
                }
                name: string = "LevelProp_brush_SRU_E18"
            }
            0xa4239dde = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6979.36475, -33.8021927, 8138.39697 }
                boxMax: vec3 = { 7173.48096, 179.977539, 8332.5127 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    7076.42285, -33.6283493, 8235.45508, 1
                }
                name: string = "LevelProp_brush_SRU_I22"
            }
            0x8f241026 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6947.52637, -48.0089188, 7994.53906 }
                boxMax: vec3 = { 7080.02539, 94.9896317, 8127.03808 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    7013.77588, -48.6737595, 8060.78857, 1
                }
                name: string = "LevelProp_brush_SRU_G43"
            }
            0xd0b0fb94 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6747.6748, -48.0084915, 8050.45312 }
                boxMax: vec3 = { 6880.17383, 94.9900589, 8182.95215 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    6813.92432, -48.6733322, 8116.70264, 1
                }
                name: string = "LevelProp_brush_SRU_G46"
            }
            0x170726d9 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7927.95557, -46.3115158, 8227.31055 }
                boxMax: vec3 = { 8136.99951, 167.294373, 8436.35352 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.859185994, 0, -0.160011321, 0
                    0, 1, 0, 0
                    0.160011321, 0, 0.859185994, 0
                    8032.47754, -46.3115158, 8331.83203, 1
                }
                name: string = "LevelProp_brush_SRU_A6"
            }
            0x70589108 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8599.04688, -43.1349335, 3038.80884 }
                boxMax: vec3 = { 8762.48828, 163.626938, 3202.25073 }
                0xad304db5: string = "Characters/brush_SRU_J/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8680.76758, -42.9611664, 3120.52978, 1
                }
                name: string = "LevelProp_brush_SRU_J8"
            }
            0x9d5956a7 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10591.3584, -46.3112793, 4164.25439 }
                boxMax: vec3 = { 10835.4228, 167.294617, 4408.31885 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    10713.3906, -46.3112793, 4286.28662, 1
                }
                name: string = "LevelProp_brush_SRU_A24"
            }
            0x993b695a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8199.8877, -103.431824, 9420.23535 }
                boxMax: vec3 = { 8387.84668, 110.174072, 9608.19434 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    8293.86719, -103.431824, 9514.21484, 1
                }
                name: string = "LevelProp_brush_SRU_A41"
            }
            0xa78df64b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7965.81104, -46.3116074, 9317.61816 }
                boxMax: vec3 = { 8149.48584, 131.081085, 9501.29394 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    8057.64844, -46.3116074, 9409.45605, 1
                }
                name: string = "LevelProp_brush_SRU_D33"
            }
            0x5ccb89d5 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7551.64551, -46.6969261, 5796.11621 }
                boxMax: vec3 = { 7752.41113, 155.045959, 5996.88184 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    7652.02832, -46.310936, 5896.49902, 1
                }
                name: string = "LevelProp_brush_SRU_F11"
            }
            0x67be95e5 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7272.38623, -48.0081863, 5866.57178 }
                boxMax: vec3 = { 7404.88525, 94.9903641, 5999.0708 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    7338.63574, -48.673027, 5932.82129, 1
                }
                name: string = "LevelProp_brush_SRU_G17"
            }
            0xa6f1bad0 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7904.23389, -49.1507721, 8164.80908 }
                boxMax: vec3 = { 8057.31494, 174.461243, 8317.88965 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.859185994, 0, -0.160011321, 0
                    0, 1, 0, 0
                    0.160011321, 0, 0.859185994, 0
                    7980.77441, -46.3113327, 8241.34961, 1
                }
                name: string = "LevelProp_brush_SRU_C21"
            }
            0x33cfa384 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7996.49756, -46.3112717, 8005.15234 }
                boxMax: vec3 = { 8168.41455, 131.081421, 8177.06934 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.859185994, 0, -0.160011321, 0
                    0, 1, 0, 0
                    0.160011321, 0, 0.859185994, 0
                    8082.45605, -46.3112717, 8091.11084, 1
                }
                name: string = "LevelProp_brush_SRU_D39"
            }
            0x6ba5692a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10769.918, -46.6974525, 4245.09326 }
                boxMax: vec3 = { 10963.9512, 155.045425, 4439.12646 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    10866.9346, -46.3114624, 4342.10986, 1
                }
                name: string = "LevelProp_brush_SRU_F16"
            }
            0x518efd6f = GdsMapObject {
                type: u8 = 1
                boxMin: vec3 = { 13426.668, 1.58190918, 9176.61426 }
                boxMax: vec3 = { 13521.291, 285.3078, 9271.2373 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    13473.9795, 1.58190918, 9223.92578, 1
                }
                name: string = "__Spawn_T2"
            }
            0xe03b375e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6476.32422, -65.5799179, 3080.17114 }
                boxMax: vec3 = { 6723.16894, 148.199829, 3327.01587 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.442454994, 0, 0.753682196, 0
                    0, 1, 0, 0
                    -0.753682196, 0, 0.442454994, 0
                    6599.74658, -65.4060745, 3203.59351, 1
                }
                name: string = "LevelProp_brush_SRU_I11"
            }
            0x19d019c6 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7364.04394, -49.1502304, 3014.03003 }
                boxMax: vec3 = { 7532.04199, 174.461792, 3182.02856 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.822188079, 0, 0.296327591, 0
                    0, 1, 0, 0
                    -0.296327591, 0, 0.822188079, 0
                    7448.04297, -46.310791, 3098.0293, 1
                }
                name: string = "LevelProp_brush_SRU_C8"
            }
            0x825bfc50 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6453.67773, -65.5798569, 2884.85083 }
                boxMax: vec3 = { 6700.52246, 148.19989, 3131.69556 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.442454994, 0, 0.753682196, 0
                    0, 1, 0, 0
                    -0.753682196, 0, 0.442454994, 0
                    6577.1001, -65.4060135, 3008.27319, 1
                }
                name: string = "LevelProp_brush_SRU_I12"
            }
            0xdd9633e2 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10539.791, -49.1509628, 4306.63281 }
                boxMax: vec3 = { 10718.5176, 174.46106, 4485.35938 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    10629.1543, -46.3115234, 4395.99609, 1
                }
                name: string = "LevelProp_brush_SRU_C11"
            }
            0xa027a83a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8500.77051, -49.1520309, 3050.45459 }
                boxMax: vec3 = { 8635.77832, 174.459991, 3185.4624 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8568.27441, -46.3125916, 3117.9585, 1
                }
                name: string = "LevelProp_brush_SRU_C10"
            }
            0x01b4d03f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9457.93555, -59.8551178, 4621.07568 }
                boxMax: vec3 = { 9631.69141, 83.1434326, 4794.82959 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.655681968, 0, 0.5778265, 0
                    0, 1, 0, 0
                    -0.5778265, 0, 0.655681968, 0
                    9544.81348, -60.5199585, 4707.95264, 1
                }
                name: string = "LevelProp_brush_SRU_G6"
            }
            0xb265e44d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7056.51367, -46.6968498, 8173.10693 }
                boxMax: vec3 = { 7302.63184, 155.046021, 8419.22558 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.79900521, 0, 0.354113579, 0
                    0, 1, 0, 0
                    -0.354113579, 0, 0.79900521, 0
                    7179.57275, -46.3108597, 8296.16602, 1
                }
                name: string = "LevelProp_brush_SRU_F31"
            }
            0xcc261494 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10631.9092, -46.4091644, 4406.29248 }
                boxMax: vec3 = { 10842.2119, 135.868851, 4616.59521 }
                0xad304db5: string = "Characters/brush_SRU_E/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    10737.0605, -46.3116455, 4511.44385, 1
                }
                name: string = "LevelProp_brush_SRU_E11"
            }
            0xaf5537b5 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10710.7949, -46.3113403, 4349.78808 }
                boxMax: vec3 = { 10897.2539, 167.294556, 4536.24805 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    10804.0244, -46.3113403, 4443.01807, 1
                }
                name: string = "LevelProp_brush_SRU_A21"
            }
            0x731fad81 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8067.73926, -46.3107948, 4590.88476 }
                boxMax: vec3 = { 8314.70215, 167.295105, 4837.84766 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.462554663, 0, 0.741517842, 0
                    0, 1, 0, 0
                    -0.741517842, 0, 0.462554663, 0
                    8191.2207, -46.3107948, 4714.36621, 1
                }
                name: string = "LevelProp_brush_SRU_A10"
            }
            0x11b97523 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5339.60254, -112.75174, 4788.85547 }
                boxMax: vec3 = { 5555.9707, 94.0101318, 5005.22363 }
                0xad304db5: string = "Characters/brush_SRU_J/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    5447.78662, -112.577972, 4897.03955, 1
                }
                name: string = "LevelProp_brush_SRU_J10"
            }
            0xf885e221 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7661.87158, -46.3105698, 5956.22558 }
                boxMax: vec3 = { 7820.53662, 131.082123, 6114.89062 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    7741.2041, -46.3105698, 6035.5581, 1
                }
                name: string = "LevelProp_brush_SRU_D11"
            }
            0x778a5381 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 8926.00976, -41.4762573, 3669.24707 }
                boxMax: vec3 = { 9020.63281, 242.249634, 3763.86914 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    8973.32129, -41.4760017, 3756.5581, 1
                }
                name: string = "__NAV_R008"
            }
            0x36e3d86b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6964.72168, -50.6297836, 9354.5 }
                boxMax: vec3 = { 7102.3623, 172.982239, 9492.14062 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    7033.54199, -47.7903442, 9423.32031, 1
                }
                name: string = "LevelProp_brush_SRU_C190"
            }
            0xd5671d54 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7438.9165, -46.3110352, 3071.81616 }
                boxMax: vec3 = { 7668.33057, 167.294861, 3301.23071 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.822188079, 0, 0.296327591, 0
                    0, 1, 0, 0
                    -0.296327591, 0, 0.822188079, 0
                    7553.62354, -46.3110352, 3186.52344, 1
                }
                name: string = "LevelProp_brush_SRU_A13"
            }
            0xa99d68e6 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8115.59766, -46.3114433, 4631.81543 }
                boxMax: vec3 = { 8320.86133, 131.081253, 4837.0791 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.500265956, 0, 0.716616213, 0
                    0, 1, 0, 0
                    -0.716616213, 0, 0.500265956, 0
                    8218.22949, -46.3114433, 4734.44726, 1
                }
                name: string = "LevelProp_brush_SRU_D4"
            }
            0xb0df6bac = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 11054.4932, -48.009079, 4675.76172 }
                boxMax: vec3 = { 11182.5498, 94.9894714, 4803.81738 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    11118.5215, -48.6739197, 4739.78955, 1
                }
                name: string = "LevelProp_brush_SRU_G26"
            }
            0x7a3e8928 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9588.84082, -36.4953003, 4802.94092 }
                boxMax: vec3 = { 9752.09473, 192.749603, 4966.19482 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    9670.46777, -36.4953003, 4884.56787, 1
                }
                name: string = "LevelProp_brush_SRU_B242"
            }
            0x1d1205ff = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8096.23389, -43.7531433, 9304.32812 }
                boxMax: vec3 = { 8250.81152, 133.639557, 9458.90625 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872872114, 0, 0.0435257256, 0
                    0, 1, 0, 0
                    -0.0435257256, 0, 0.872872114, 0
                    8173.52246, -43.7531433, 9381.61719, 1
                }
                name: string = "LevelProp_brush_SRU_D32"
            }
            0x0a1331f6 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4540.21533, -49.151535, 8225.47168 }
                boxMax: vec3 = { 4703.76514, 174.46048, 8389.02051 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    4621.99023, -46.3120956, 8307.24609, 1
                }
                name: string = "LevelProp_brush_SRU_C6"
            }
            0xbd7ebb1d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8609.04394, -46.6988869, 3022.5708 }
                boxMax: vec3 = { 8800.89551, 155.043991, 3214.42285 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8704.96973, -46.3128967, 3118.49683, 1
                }
                name: string = "LevelProp_brush_SRU_F19"
            }
            0x980aca23 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6887.69189, -46.3111191, 7997.50879 }
                boxMax: vec3 = { 7046.35693, 131.081573, 8156.17383 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    6967.02441, -46.3111191, 8076.84131, 1
                }
                name: string = "LevelProp_brush_SRU_D29"
            }
            0xd45145ca = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6828.97558, -46.3112411, 8111.73389 }
                boxMax: vec3 = { 7021.9043, 167.294647, 8304.66211 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    6925.43994, -46.3112411, 8208.19824, 1
                }
                name: string = "LevelProp_brush_SRU_A34"
            }
            0x0a753645 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9334.78808, -65.5805664, 4587.30078 }
                boxMax: vec3 = { 9589.34668, 148.199173, 4841.8584 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.655681968, 0, 0.5778265, 0
                    0, 1, 0, 0
                    -0.5778265, 0, 0.655681968, 0
                    9462.06738, -65.406723, 4714.57959, 1
                }
                name: string = "LevelProp_brush_SRU_I3"
            }
            0x6579fb59 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8180.51562, -94.4789429, 9336.28027 }
                boxMax: vec3 = { 8368.47461, 119.126953, 9524.23926 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    8274.49512, -94.4789429, 9430.25976, 1
                }
                name: string = "LevelProp_brush_SRU_A11"
            }
            0x9c36c202 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7047.45605, -46.3106155, 8143.79736 }
                boxMax: vec3 = { 7241.96289, 131.082092, 8338.30469 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.79900521, 0, 0.354113579, 0
                    0, 1, 0, 0
                    -0.354113579, 0, 0.79900521, 0
                    7144.70947, -46.3106155, 8241.05078, 1
                }
                name: string = "LevelProp_brush_SRU_D38"
            }
            0x8458d91a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8120.89307, -46.3111496, 8171.95166 }
                boxMax: vec3 = { 8292.81055, 131.081543, 8343.86914 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.859185994, 0, -0.160011321, 0
                    0, 1, 0, 0
                    0.160011321, 0, 0.859185994, 0
                    8206.85156, -46.3111496, 8257.91016, 1
                }
                name: string = "LevelProp_brush_SRU_D37"
            }
            0xfd551ad8 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6580.89502, -46.3116455, 3027.63623 }
                boxMax: vec3 = { 6832.1792, 167.29425, 3278.9209 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.694166541, 0, 0.530976534, 0
                    0, 1, 0, 0
                    -0.530976534, 0, 0.694166541, 0
                    6706.53711, -46.3116455, 3153.27856, 1
                }
                name: string = "LevelProp_brush_SRU_A14"
            }
            0xe1b3f21f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4477.83398, -46.4094086, 4243.22119 }
                boxMax: vec3 = { 4688.13672, 135.868607, 4453.52392 }
                0xad304db5: string = "Characters/brush_SRU_E/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    4582.98535, -46.3118896, 4348.37256, 1
                }
                name: string = "LevelProp_brush_SRU_E2"
            }
            0x58a3f7fe = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5351.26318, -46.4077606, 4890.32324 }
                boxMax: vec3 = { 5561.56592, 135.870255, 5100.62598 }
                0xad304db5: string = "Characters/brush_SRU_E/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    5456.41455, -46.3102417, 4995.47461, 1
                }
                name: string = "LevelProp_brush_SRU_E13"
            }
            0x979f392d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4154.6831, -46.3118896, 4493.58203 }
                boxMax: vec3 = { 4398.74756, 167.294006, 4737.64648 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    4276.71533, -46.3118896, 4615.61426, 1
                }
                name: string = "LevelProp_brush_SRU_A2"
            }
            0xae5c3a97 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10593.8271, -46.3112793, 4420.91943 }
                boxMax: vec3 = { 10794.5459, 131.081421, 4621.63916 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    10694.1865, -46.3112793, 4521.2793, 1
                }
                name: string = "LevelProp_brush_SRU_D17"
            }
            0x1a81f31d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9604.48926, -46.3119278, 4898.87695 }
                boxMax: vec3 = { 9824.2373, 182.932983, 5118.62402 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.655681968, 0, 0.5778265, 0
                    0, 1, 0, 0
                    -0.5778265, 0, 0.655681968, 0
                    9714.36328, -46.3119278, 5008.75049, 1
                }
                name: string = "LevelProp_brush_SRU_B7"
            }
            0x91ba298c = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5566.00195, -46.3122177, 10117.9414 }
                boxMax: vec3 = { 5749.67676, 131.080475, 10301.6172 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    5657.83936, -46.3122177, 10209.7793, 1
                }
                name: string = "LevelProp_brush_SRU_D22"
            }
            0x6545727b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9474.86426, -46.4330521, 10031.6318 }
                boxMax: vec3 = { 9647.15137, 135.844971, 10203.9189 }
                0xad304db5: string = "Characters/brush_SRU_E/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    9561.00781, -46.3355331, 10117.7754, 1
                }
                name: string = "LevelProp_brush_SRU_E16"
            }
            0xeb467e93 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7972.63428, -59.8545227, 8104.13867 }
                boxMax: vec3 = { 8116.19971, 83.1440277, 8247.7041 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.859185994, 0, -0.160011321, 0
                    0, 1, 0, 0
                    0.160011321, 0, 0.859185994, 0
                    8044.41699, -60.5193634, 8175.92139, 1
                }
                name: string = "LevelProp_brush_SRU_G60"
            }
            0x2d49ee20 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9482.26074, -46.3133469, 9950.07324 }
                boxMax: vec3 = { 9682.20801, 167.292542, 10150.0205 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    9582.23438, -46.3133469, 10050.0469, 1
                }
                name: string = "LevelProp_brush_SRU_A31"
            }
            0xa92ce3b2 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8029.9873, -48.0082397, 8043.92969 }
                boxMax: vec3 = { 8167.7373, 94.9903107, 8181.67969 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.866878152, 0, -0.11102581, 0
                    0, 1, 0, 0
                    0.11102581, 0, 0.866878152, 0
                    8098.8623, -48.6730804, 8112.80469, 1
                }
                name: string = "LevelProp_brush_SRU_G49"
            }
            0x9e042a5b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8236.15527, -46.3109283, 7926.3457 }
                boxMax: vec3 = { 8410.36621, 182.933975, 8100.55762 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.866878152, 0, -0.11102581, 0
                    0, 1, 0, 0
                    0.11102581, 0, 0.866878152, 0
                    8323.26074, -46.3109283, 8013.45166, 1
                }
                name: string = "LevelProp_brush_SRU_B27"
            }
            0x080956c9 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7556.81348, -43.1334, 5924.65723 }
                boxMax: vec3 = { 7727.84863, 163.628479, 6095.69238 }
                0xad304db5: string = "Characters/brush_SRU_J/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    7642.33105, -42.9596329, 6010.1748, 1
                }
                name: string = "LevelProp_brush_SRU_J5"
            }
            0x25eaf882 = GdsMapObject {
                type: u8 = 5
                boxMin: vec3 = { 3673.91138, -525.081848, 6144.95166 }
                boxMax: vec3 = { 3970.76147, 457.882111, 6441.80127 }
                0xad304db5: string = "Characters/SRUAP_Turret_Chaos1/Skins/Skin11"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.0845125467, 0, -0.99642241, 0
                    0, 1, 0, 0
                    0.99642241, 0, 0.0845125467, 0
                    3822.33594, -8, 6293.37598, 1
                }
                name: string = "Turret_T1_C_02"
            }
            0xec45c7be = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6339.76855, -43.1338654, 2877.39844 }
                boxMax: vec3 = { 6543.14941, 163.628006, 3080.77881 }
                0xad304db5: string = "Characters/brush_SRU_J/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.822188079, 0, 0.296327591, 0
                    0, 1, 0, 0
                    -0.296327591, 0, 0.822188079, 0
                    6441.45898, -42.9600983, 2979.08862, 1
                }
                name: string = "LevelProp_brush_SRU_J6"
            }
            0x4a345513 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9679.23047, -36.4961548, 4822.14014 }
                boxMax: vec3 = { 9867.18945, 177.109741, 5010.09912 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    9773.20996, -36.4961548, 4916.11963, 1
                }
                name: string = "LevelProp_brush_SRU_A238"
            }
            0x8a076d50 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 6186.76025, -41.475769, 3715.2876 }
                boxMax: vec3 = { 6281.38232, 242.250122, 3809.90967 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    6234.07129, -41.475769, 3762.59863, 1
                }
                name: string = "__NAV_R005"
            }
            0xa7fdc523 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7349.18652, -48.0088959, 6006.29443 }
                boxMax: vec3 = { 7475.66992, 94.9896545, 6132.77783 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873620808, 0, 0.0243072212, 0
                    0, 1, 0, 0
                    -0.0243072212, 0, 0.873620808, 0
                    7412.42822, -48.6737366, 6069.53613, 1
                }
                name: string = "LevelProp_brush_SRU_G11"
            }
            0x8af10182 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8675.92285, -65.5811081, 2861.65747 }
                boxMax: vec3 = { 8861.4209, 148.198639, 3047.15552 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8768.67188, -65.4072647, 2954.40649, 1
                }
                name: string = "LevelProp_brush_SRU_I16"
            }
            0xb9f608a0 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6990.20166, -103.432861, 9367.33301 }
                boxMax: vec3 = { 7178.16064, 110.173035, 9555.29199 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    7084.18115, -103.432861, 9461.3125, 1
                }
                name: string = "LevelProp_brush_SRU_A100"
            }
            0x415888a2 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9291.50976, -48.0092392, 4619.34717 }
                boxMax: vec3 = { 9465.26562, 94.9893112, 4793.10107 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.655681968, 0, 0.5778265, 0
                    0, 1, 0, 0
                    -0.5778265, 0, 0.655681968, 0
                    9378.3877, -48.6740799, 4706.22412, 1
                }
                name: string = "LevelProp_brush_SRU_G5"
            }
            0xf2ddce56 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 11779.0391, -41.4771118, 6731.27832 }
                boxMax: vec3 = { 11873.6621, 242.248779, 6825.90039 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    11626.3506, -41.4770012, 6850, 1
                }
                name: string = "__NAV_L007"
            }
            0x16e6b578 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8013.05029, -48.1603394, 9372.96875 }
                boxMax: vec3 = { 8167.62744, 129.232361, 9527.54688 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    8090.33887, -48.1603394, 9450.25781, 1
                }
                name: string = "LevelProp_brush_SRU_D31"
            }
            0xa1588dbd = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5518.21924, -46.3120346, 9984.13086 }
                boxMax: vec3 = { 5701.89404, 131.080658, 10167.8066 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    5610.05664, -46.3120346, 10075.9688, 1
                }
                name: string = "LevelProp_brush_SRU_D21"
            }
            0x407c54dd = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6919.90283, -49.1500549, 7973.81445 }
                boxMax: vec3 = { 7093.09814, 174.461975, 8147.01074 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.79900521, 0, 0.354113579, 0
                    0, 1, 0, 0
                    -0.354113579, 0, 0.79900521, 0
                    7006.50049, -46.3106155, 8060.4126, 1
                }
                name: string = "LevelProp_brush_SRU_C19"
            }
            0x39decb8e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5271.72168, -46.3101196, 4782.77734 }
                boxMax: vec3 = { 5515.78613, 167.295776, 5026.8418 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    5393.75391, -46.3101196, 4904.80957, 1
                }
                name: string = "LevelProp_brush_SRU_A29"
            }
            0x487bba11 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10745.8486, -48.0089569, 4544.38379 }
                boxMax: vec3 = { 10873.9053, 94.9895935, 4672.43945 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    10809.877, -48.6737976, 4608.41162, 1
                }
                name: string = "LevelProp_brush_SRU_G23"
            }
            0xcdb9a0f6 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10788.252, -46.4317169, 4515.68408 }
                boxMax: vec3 = { 10948.918, 135.846298, 4676.3501 }
                0xad304db5: string = "Characters/brush_SRU_E/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    10868.585, -46.334198, 4596.01709, 1
                }
                name: string = "LevelProp_brush_SRU_E8"
            }
            0x4478ab17 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 9906.25586, -41.4772339, 4129.2373 }
                boxMax: vec3 = { 10000.8789, 242.248657, 4223.85938 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    9953.56738, -41.4770012, 4376.54785, 1
                }
                name: string = "__NAV_R009"
            }
            0x85700cda = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9553.77637, -46.3131027, 10096.4551 }
                boxMax: vec3 = { 9718.21387, 131.07959, 10260.8926 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    9635.99512, -46.3131027, 10178.6738, 1
                }
                name: string = "LevelProp_brush_SRU_D23"
            }
            0x3755bcb4 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 2934.95679, -41.4772339, 6418.25928 }
                boxMax: vec3 = { 3029.57886, 242.248657, 6512.88135 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    2982.26782, -41.4772339, 6465.57031, 1
                }
                name: string = "__NAV_R002"
            }
            0xcb270248 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4311.56885, -47.4317017, 4236.64844 }
                boxMax: vec3 = { 4474.82275, 181.813202, 4399.90234 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    4393.1958, -47.4317017, 4318.27539, 1
                }
                name: string = "LevelProp_brush_SRU_B42"
            }
            0xd38907f8 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 2044.65503, -41.480896, 7459.9375 }
                boxMax: vec3 = { 2139.2771, 242.244995, 7554.55957 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    1591.96594, -41.480999, 7507.24902, 1
                }
                name: string = "__NAV_R001"
            }
            0x469579cb = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4510.47412, -46.432106, 8383.14648 }
                boxMax: vec3 = { 4702.91846, 135.845917, 8575.58984 }
                0xad304db5: string = "Characters/brush_SRU_E/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    4606.69629, -46.3345871, 8479.36816, 1
                }
                name: string = "LevelProp_brush_SRU_E14"
            }
            0xb6eb0b75 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5365.75732, -46.3125839, 10002.8525 }
                boxMax: vec3 = { 5559.74268, 182.932312, 10196.8369 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    5462.75, -46.3125839, 10099.8447, 1
                }
                name: string = "LevelProp_brush_SRU_B10"
            }
            0x1d29d933 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9599.55273, -48.0103531, 10033.4404 }
                boxMax: vec3 = { 9736.87109, 94.9881973, 10170.7588 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    9668.21191, -48.6751938, 10102.0996, 1
                }
                name: string = "LevelProp_brush_SRU_G38"
            }
            0xfbe3ccfe = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7570.14307, -43.1339264, 6019.24756 }
                boxMax: vec3 = { 7733.41455, 163.627945, 6182.51904 }
                0xad304db5: string = "Characters/brush_SRU_J/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873620808, 0, 0.0243072212, 0
                    0, 1, 0, 0
                    -0.0243072212, 0, 0.873620808, 0
                    7651.77881, -42.9601593, 6100.8833, 1
                }
                name: string = "LevelProp_brush_SRU_J4"
            }
            0xc9a1c7b2 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8191.50293, -43.1334534, 8021.26855 }
                boxMax: vec3 = { 8369.31543, 163.628418, 8199.08105 }
                0xad304db5: string = "Characters/brush_SRU_J/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.866878152, 0, -0.11102581, 0
                    0, 1, 0, 0
                    0.11102581, 0, 0.866878152, 0
                    8280.40918, -42.9596863, 8110.1748, 1
                }
                name: string = "LevelProp_brush_SRU_J15"
            }
            0x151a1033 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7744.37695, -48.0084305, 5793.31885 }
                boxMax: vec3 = { 7876.87598, 94.9901199, 5925.81787 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    7810.62646, -48.6732712, 5859.56836, 1
                }
                name: string = "LevelProp_brush_SRU_G18"
            }
            0xbb9ec541 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10369.0986, -65.5818634, 8403.9502 }
                boxMax: vec3 = { 10570.2764, 148.197876, 8605.12793 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    10469.6875, -65.40802, 8504.53906, 1
                }
                name: string = "LevelProp_brush_SRU_I18"
            }
            0xf67d5730 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9606.4375, -48.0105362, 9979.36035 }
                boxMax: vec3 = { 9743.75586, 94.9880142, 10116.6787 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    9675.09668, -48.6753769, 10048.0195, 1
                }
                name: string = "LevelProp_brush_SRU_G39"
            }
            0x717020cb = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8456.94922, -59.8559036, 3011.28418 }
                boxMax: vec3 = { 8583.56641, 83.1426468, 3137.90039 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8520.25781, -60.5207443, 3074.59228, 1
                }
                name: string = "LevelProp_brush_SRU_G30"
            }
            0x8c4febc8 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7386.74902, -46.6975746, 5983.74072 }
                boxMax: vec3 = { 7578.40039, 155.045303, 6175.39209 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873620808, 0, 0.0243072212, 0
                    0, 1, 0, 0
                    -0.0243072212, 0, 0.873620808, 0
                    7482.57471, -46.3115845, 6079.56641, 1
                }
                name: string = "LevelProp_brush_SRU_F1"
            }
            0x69e63cef = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8172.86572, -65.5798798, 9189.91406 }
                boxMax: vec3 = { 8397.5791, 148.19986, 9414.62695 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    8285.22266, -65.4060364, 9302.27051, 1
                }
                name: string = "LevelProp_brush_SRU_I26"
            }
            0xfc606692 = GdsMapObject {
                type: u8 = 5
                boxMin: vec3 = { 5538.9834, -533.805359, 3633.84692 }
                boxMax: vec3 = { 5984.09521, 471.081909, 4075.02783 }
                0xad304db5: string = "Characters/SRUAP_Turret_Chaos1/Skins/Skin11"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.60816586, 0, -0.79380995, 0
                    0, 1, 0, 0
                    0.79380995, 0, 0.60816586, 0
                    5762.16699, -8, 3855.0249, 1
                }
                name: string = "Turret_T1_C_03"
            }
            0x4b5b986a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4034.65698, -49.1510849, 4487.96924 }
                boxMax: vec3 = { 4213.38379, 174.460938, 4666.6958 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    4124.02051, -46.3116455, 4577.33252, 1
                }
                name: string = "LevelProp_brush_SRU_C1"
            }
            0x8cb5e37c = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5434.45654, -46.3122177, 9965.54199 }
                boxMax: vec3 = { 5618.13135, 131.080475, 10149.2178 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    5526.29394, -46.3122177, 10057.3799, 1
                }
                name: string = "LevelProp_brush_SRU_D9"
            }
            0xe084607f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10912.5771, -46.3117676, 4602.84473 }
                boxMax: vec3 = { 11099.0361, 167.294128, 4789.30469 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    11005.8066, -46.3117676, 4696.07471, 1
                }
                name: string = "LevelProp_brush_SRU_A17"
            }
            0xf726683e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8881.91797, -48.0097198, 3108.82983 }
                boxMax: vec3 = { 9008.53516, 94.9888306, 3235.44604 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8945.22656, -48.6745605, 3172.13794, 1
                }
                name: string = "LevelProp_brush_SRU_G28"
            }
            0x1732ecd6 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 12026.4726, -41.4765015, 6354.41602 }
                boxMax: vec3 = { 12121.0957, 242.24939, 6449.03808 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    12273.7842, -41.4770012, 6401.72705, 1
                }
                name: string = "__NAV_R011"
            }
            0x8f18d42b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6840.10693, -43.1338882, 8083.50684 }
                boxMax: vec3 = { 7011.14209, 163.627991, 8254.54199 }
                0xad304db5: string = "Characters/brush_SRU_J/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    6925.62451, -42.9601212, 8169.02441, 1
                }
                name: string = "LevelProp_brush_SRU_J14"
            }
            0x7350d08b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4562.9585, -65.5808563, 8355.58105 }
                boxMax: vec3 = { 4787.67334, 148.198883, 8580.29394 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    4675.31592, -65.4070129, 8467.9375, 1
                }
                name: string = "LevelProp_brush_SRU_I5"
            }
            0xa731a603 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7550.23682, -46.3114624, 6062.57715 }
                boxMax: vec3 = { 7734.40771, 167.294434, 6246.74805 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873620808, 0, 0.0243072212, 0
                    0, 1, 0, 0
                    -0.0243072212, 0, 0.873620808, 0
                    7642.32226, -46.3114624, 6154.6626, 1
                }
                name: string = "LevelProp_brush_SRU_A1"
            }
            0x6cf91d49 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7991.68994, -59.8551025, 9425.07129 }
                boxMax: vec3 = { 8145.07373, 83.1434479, 9578.45605 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    8068.38184, -60.5199432, 9501.76367, 1
                }
                name: string = "LevelProp_brush_SRU_G53"
            }
            0x955db396 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8163.75537, -46.3109894, 8032.65771 }
                boxMax: vec3 = { 8337.9668, 182.933914, 8206.86914 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.866878152, 0, -0.11102581, 0
                    0, 1, 0, 0
                    0.11102581, 0, 0.866878152, 0
                    8250.86133, -46.3109894, 8119.76367, 1
                }
                name: string = "LevelProp_brush_SRU_B25"
            }
            0xb04550a8 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7980.03223, -46.697506, 8055.6001 }
                boxMax: vec3 = { 8197.56738, 155.04538, 8273.13476 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.859185994, 0, -0.160011321, 0
                    0, 1, 0, 0
                    0.160011321, 0, 0.859185994, 0
                    8088.7998, -46.3115158, 8164.36768, 1
                }
                name: string = "LevelProp_brush_SRU_F33"
            }
            0x4ce193f3 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7038.12598, -46.3107986, 8151.75195 }
                boxMax: vec3 = { 7274.6377, 167.295105, 8388.26367 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.79900521, 0, 0.354113579, 0
                    0, 1, 0, 0
                    -0.354113579, 0, 0.79900521, 0
                    7156.38184, -46.3107986, 8270.00781, 1
                }
                name: string = "LevelProp_brush_SRU_A18"
            }
            0x9b6deb34 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4705.09228, -46.3120956, 8299.83105 }
                boxMax: vec3 = { 4899.07764, 182.9328, 8493.81543 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    4802.08496, -46.3120956, 8396.82324, 1
                }
                name: string = "LevelProp_brush_SRU_B16"
            }
            0x1820dd53 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8180.81445, -63.9835205, 9268.08105 }
                boxMax: vec3 = { 8368.77344, 149.622375, 9456.04004 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    8274.79394, -63.9835205, 9362.06055, 1
                }
                name: string = "LevelProp_brush_SRU_A39"
            }
            0xa1eb9eed = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6807.57324, -49.1505585, 7981.80518 }
                boxMax: vec3 = { 6948.85352, 174.461456, 8123.08545 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    6878.21338, -46.3111191, 8052.44531, 1
                }
                name: string = "LevelProp_brush_SRU_C5"
            }
            0x515e5183 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 4035.95703, -41.4777222, 5448.94726 }
                boxMax: vec3 = { 4130.5791, 242.248169, 5543.56934 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    4083.26807, -41.4777222, 5496.2583, 1
                }
                name: string = "__NAV_R003"
            }
            0x9476fe37 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7734.72314, -46.3114624, 5972.03516 }
                boxMax: vec3 = { 7894.68701, 182.933441, 6131.99902 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873620808, 0, 0.0243072212, 0
                    0, 1, 0, 0
                    -0.0243072212, 0, 0.873620808, 0
                    7814.70508, -46.3114624, 6052.01709, 1
                }
                name: string = "LevelProp_brush_SRU_B3"
            }
            0xb44b4466 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7649.65918, -33.8017654, 5805.1001 }
                boxMax: vec3 = { 7843.77539, 179.977966, 5999.21631 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    7746.71728, -33.6279221, 5902.1582, 1
                }
                name: string = "LevelProp_brush_SRU_I9"
            }
            0x943c186a = GdsMapObject {
                type: u8 = 3
                boxMin: vec3 = { 3159.86548, -312.81488, 6230.19678 }
                boxMax: vec3 = { 3698.35718, 348.230896, 6768.68799 }
                0xad304db5: string = "Characters/SRUAP_OrderInhibitor/Skins/Skin10"
                sceneLayer: string = "Map Objects"
                transform: mtx44 = {
                    0.827416062, 0, -0.56158942, 0
                    0, 1, 0, 0
                    0.56158942, 0, 0.827416062, 0
                    3429.11133, -17.7250519, 6499.44238, 1
                }
                name: string = "Barracks_T1_R1"
            }
            0x5fce7054 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9434.68555, -46.3127975, 10023.165 }
                boxMax: vec3 = { 9599.12305, 131.079895, 10187.6025 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    9516.9043, -46.3127975, 10105.3838, 1
                }
                name: string = "LevelProp_brush_SRU_D25"
            }
            0x80591aee = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4294.02051, -65.5803452, 4292.16943 }
                boxMax: vec3 = { 4539.58691, 148.199402, 4537.73584 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    4416.80371, -65.4065018, 4414.95264, 1
                }
                name: string = "LevelProp_brush_SRU_I2"
            }
            0x4fd2b964 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4653.63037, -49.1511688, 8282.20508 }
                boxMax: vec3 = { 4817.18018, 174.460846, 8445.75391 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    4735.40527, -46.3117294, 8363.97949, 1
                }
                name: string = "LevelProp_brush_SRU_C14"
            }
            0x4a558899 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6608.43652, -48.0088348, 3077.34888 }
                boxMax: vec3 = { 6781.01172, 94.9897156, 3249.92505 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.694166541, 0, 0.530976534, 0
                    0, 1, 0, 0
                    -0.530976534, 0, 0.694166541, 0
                    6694.72412, -48.6736755, 3163.63696, 1
                }
                name: string = "LevelProp_brush_SRU_G22"
            }
            0x8b8bfcd7 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4009.30542, -46.6977577, 4560.78564 }
                boxMax: vec3 = { 4263.28418, 155.04512, 4814.76416 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    4136.29492, -46.3117676, 4687.7749, 1
                }
                name: string = "LevelProp_brush_SRU_F3"
            }
            0xa18d7b0b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8031.57764, -43.1339188, 8182.31982 }
                boxMax: vec3 = { 8216.89844, 163.62796, 8367.6416 }
                0xad304db5: string = "Characters/brush_SRU_J/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.859185994, 0, -0.160011321, 0
                    0, 1, 0, 0
                    0.160011321, 0, 0.859185994, 0
                    8124.23828, -42.9601517, 8274.98047, 1
                }
                name: string = "LevelProp_brush_SRU_J18"
            }
            0x784cbbca = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7446.1499, -46.3117065, 5999.05615 }
                boxMax: vec3 = { 7630.3208, 167.294189, 6183.22705 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873620808, 0, 0.0243072212, 0
                    0, 1, 0, 0
                    -0.0243072212, 0, 0.873620808, 0
                    7538.23535, -46.3117065, 6091.1416, 1
                }
                name: string = "LevelProp_brush_SRU_A9"
            }
            0x4da50a1d = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 10473.9434, -41.4762573, 6513.2373 }
                boxMax: vec3 = { 10568.5664, 242.249634, 6607.85938 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    10521.2549, -41.4760017, 6442.23584, 1
                }
                name: string = "__NAV_L006"
            }
            0xcc91e62b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8056.02686, -46.3114548, 8017.07373 }
                boxMax: vec3 = { 8237.59473, 182.933441, 8198.6416 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.859185994, 0, -0.160011321, 0
                    0, 1, 0, 0
                    0.160011321, 0, 0.859185994, 0
                    8146.81104, -46.3114548, 8107.85791, 1
                }
                name: string = "LevelProp_brush_SRU_B21"
            }
            0xe910e233 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10481.2568, -65.5818634, 8301.97266 }
                boxMax: vec3 = { 10682.4346, 148.197876, 8503.15039 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    10581.8457, -65.40802, 8402.56152, 1
                }
                name: string = "LevelProp_brush_SRU_I19"
            }
            0xe22d5a7a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5498.29053, -65.5810394, 9994.75488 }
                boxMax: vec3 = { 5723.00537, 148.1987, 10219.4678 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    5610.64795, -65.407196, 10107.1113, 1
                }
                name: string = "LevelProp_brush_SRU_I6"
            }
            0xf3954c63 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7352.68701, -33.8022919, 5830.47949 }
                boxMax: vec3 = { 7537.9917, 179.977448, 6015.78418 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873620808, 0, 0.0243072212, 0
                    0, 1, 0, 0
                    -0.0243072212, 0, 0.873620808, 0
                    7445.33936, -33.6284485, 5923.13184, 1
                }
                name: string = "LevelProp_brush_SRU_I8"
            }
            0x8611021d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8066.80127, -42.5149536, 9402.01367 }
                boxMax: vec3 = { 8221.37891, 134.877747, 9556.5918 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    8144.08984, -42.5149536, 9479.30273, 1
                }
                name: string = "LevelProp_brush_SRU_D14"
            }
            0xeb222dc5 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9467.04785, -46.6978569, 4752.48047 }
                boxMax: vec3 = { 9730.3252, 155.045013, 5015.75781 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.655681968, 0, 0.5778265, 0
                    0, 1, 0, 0
                    -0.5778265, 0, 0.655681968, 0
                    9598.68652, -46.3118668, 4884.11914, 1
                }
                name: string = "LevelProp_brush_SRU_F6"
            }
            0xb875a1b6 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 6627.104, -41.4760132, 6776.75586 }
                boxMax: vec3 = { 6721.72607, 242.249878, 6871.37793 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    6674.41504, -41.4760017, 6700.06689, 1
                }
                name: string = "__NAV_L004"
            }
            0xa6bf1525 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6219.53418, -48.0083466, 3042.58179 }
                boxMax: vec3 = { 6377.08984, 94.9902039, 3200.13794 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.822188079, 0, 0.296327591, 0
                    0, 1, 0, 0
                    -0.296327591, 0, 0.822188079, 0
                    6298.31201, -48.6731873, 3121.35986, 1
                }
                name: string = "LevelProp_brush_SRU_G19"
            }
            0x488ae3e0 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6980.48096, -63.9845581, 9273.31738 }
                boxMax: vec3 = { 7168.43994, 149.621338, 9461.27637 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    7074.46045, -63.9845581, 9367.29688, 1
                }
                name: string = "LevelProp_brush_SRU_A162"
            }
            0x80094fab = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6537.40674, -46.3112793, 2915.35547 }
                boxMax: vec3 = { 6755.66357, 182.933624, 3133.6123 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.694166541, 0, 0.530976534, 0
                    0, 1, 0, 0
                    -0.530976534, 0, 0.694166541, 0
                    6646.53516, -46.3112793, 3024.48389, 1
                }
                name: string = "LevelProp_brush_SRU_B14"
            }
            0x85ccdbd6 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9710.40332, -41.4793091, 4947.47607 }
                boxMax: vec3 = { 9864.98144, 135.913391, 5102.05322 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    9787.69238, -41.4793091, 5024.76465, 1
                }
                name: string = "LevelProp_brush_SRU_D19"
            }
            0xb1538ae2 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7756.28369, -48.0090179, 5906.146 }
                boxMax: vec3 = { 7882.76709, 94.9895325, 6032.62939 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873620808, 0, 0.0243072212, 0
                    0, 1, 0, 0
                    -0.0243072212, 0, 0.873620808, 0
                    7819.52539, -48.6738586, 5969.3877, 1
                }
                name: string = "LevelProp_brush_SRU_G14"
            }
            0xaf598bb8 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8007.4043, -65.579628, 7959.80078 }
                boxMax: vec3 = { 8209.21289, 148.200104, 8161.60938 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.866878152, 0, -0.11102581, 0
                    0, 1, 0, 0
                    0.11102581, 0, 0.866878152, 0
                    8108.30859, -65.4057846, 8060.70508, 1
                }
                name: string = "LevelProp_brush_SRU_I24"
            }
            0x790071c2 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 3135.84888, -41.4768677, 6802.64111 }
                boxMax: vec3 = { 3230.47095, 242.249023, 6897.26318 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    3183.15991, -41.4770012, 6850, 1
                }
                name: string = "__NAV_L002"
            }
            0xfac3d424 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 8029.99756, -41.4772339, 3586.50049 }
                boxMax: vec3 = { 8124.61963, 242.248657, 3681.12256 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    8077.30908, -41.4770012, 3533.81201, 1
                }
                name: string = "__NAV_R007"
            }
            0x7fd1c849 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8156.17871, -50.6288071, 9320.74023 }
                boxMax: vec3 = { 8293.81934, 172.983215, 9458.38086 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    8224.99902, -47.7893677, 9389.56055, 1
                }
                name: string = "LevelProp_brush_SRU_C17"
            }
            0xd420dddd = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7008.21631, -46.3111191, 8059.11523 }
                boxMax: vec3 = { 7175.7876, 182.933777, 8226.68652 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    7092.00195, -46.3111191, 8142.90088, 1
                }
                name: string = "LevelProp_brush_SRU_B26"
            }
            0xfc0bb319 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9642.75586, -46.4331741, 10031.3662 }
                boxMax: vec3 = { 9815.04297, 135.844849, 10203.6533 }
                0xad304db5: string = "Characters/brush_SRU_E/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    9728.89941, -46.3356552, 10117.5098, 1
                }
                name: string = "LevelProp_brush_SRU_E15"
            }
            0x4c6f930a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10616.3545, -46.3112793, 4263.59277 }
                boxMax: vec3 = { 10860.4189, 167.294617, 4507.65723 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    10738.3867, -46.3112793, 4385.625, 1
                }
                name: string = "LevelProp_brush_SRU_A23"
            }
            0xaccea964 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5573.96191, -46.3124619, 10048.1777 }
                boxMax: vec3 = { 5767.94726, 182.932434, 10242.1621 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    5670.95459, -46.3124619, 10145.1699, 1
                }
                name: string = "LevelProp_brush_SRU_B8"
            }
            0x1a0ae3d7 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6320.07715, -46.3112793, 3008.02173 }
                boxMax: vec3 = { 6519.33789, 182.933624, 3207.28296 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.822188079, 0, 0.296327591, 0
                    0, 1, 0, 0
                    -0.296327591, 0, 0.822188079, 0
                    6419.70752, -46.3112793, 3107.65234, 1
                }
                name: string = "LevelProp_brush_SRU_B13"
            }
            0x5543af67 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10827.2695, -59.8547134, 4337.93701 }
                boxMax: vec3 = { 10955.3262, 83.143837, 4465.99268 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    10891.2978, -60.5195541, 4401.96484, 1
                }
                name: string = "LevelProp_brush_SRU_G31"
            }
            0x415c2c67 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4543.54004, -59.8554077, 8189.74951 }
                boxMax: vec3 = { 4696.92383, 83.1431427, 8343.13379 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    4620.23193, -60.5202484, 8266.44141, 1
                }
                name: string = "LevelProp_brush_SRU_G10"
            }
            0xa93a576e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5358.71484, -49.1500473, 4738.02881 }
                boxMax: vec3 = { 5537.44141, 174.461975, 4916.75537 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    5448.07812, -46.3106079, 4827.39209, 1
                }
                name: string = "LevelProp_brush_SRU_C12"
            }
            0xfbcdd9f3 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6286.14844, -46.6973915, 3055.36279 }
                boxMax: vec3 = { 6524.88086, 155.045486, 3294.09619 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.822188079, 0, 0.296327591, 0
                    0, 1, 0, 0
                    -0.296327591, 0, 0.822188079, 0
                    6405.51465, -46.3114014, 3174.72949, 1
                }
                name: string = "LevelProp_brush_SRU_F14"
            }
            0xa42e6669 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7489.99756, -46.3114624, 6000.26416 }
                boxMax: vec3 = { 7649.96142, 182.933441, 6160.22803 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873620808, 0, 0.0243072212, 0
                    0, 1, 0, 0
                    -0.0243072212, 0, 0.873620808, 0
                    7569.97949, -46.3114624, 6080.24609, 1
                }
                name: string = "LevelProp_brush_SRU_B2"
            }
            0xf915618c = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 4638.5752, -41.4777222, 6444.9248 }
                boxMax: vec3 = { 4733.19726, 242.248169, 6539.54688 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    4685.88623, -41.4780006, 6442.23584, 1
                }
                name: string = "__NAV_L003"
            }
            0xe57b9d04 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9182.99512, -46.4317551, 4698.1665 }
                boxMax: vec3 = { 9400.99707, 135.846252, 4916.16846 }
                0xad304db5: string = "Characters/brush_SRU_E/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.655681968, 0, 0.5778265, 0
                    0, 1, 0, 0
                    -0.5778265, 0, 0.655681968, 0
                    9291.99609, -46.3342361, 4807.16748, 1
                }
                name: string = "LevelProp_brush_SRU_E3"
            }
            0x75cea5b6 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4115.00049, -46.4317169, 4632.36963 }
                boxMax: vec3 = { 4325.30322, 135.846298, 4842.67236 }
                0xad304db5: string = "Characters/brush_SRU_E/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    4220.15186, -46.334198, 4737.521, 1
                }
                name: string = "LevelProp_brush_SRU_E1"
            }
            0x00791f13 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9583.43262, -46.3130417, 10042.0859 }
                boxMax: vec3 = { 9747.87012, 131.079651, 10206.5234 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    9665.65137, -46.3130417, 10124.3047, 1
                }
                name: string = "LevelProp_brush_SRU_D26"
            }
            0xe532b6dc = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10864.1123, -46.3113403, 4321.18408 }
                boxMax: vec3 = { 11050.5713, 167.294556, 4507.64404 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    10957.3418, -46.3113403, 4414.41406, 1
                }
                name: string = "LevelProp_brush_SRU_A22"
            }
            0x6d556348 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5523.43018, -40.1118393, 4643.13721 }
                boxMax: vec3 = { 5739.79834, 166.650024, 4859.50537 }
                0xad304db5: string = "Characters/brush_SRU_J/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    5631.61426, -39.9380722, 4751.32129, 1
                }
                name: string = "LevelProp_brush_SRU_J12"
            }
            0xece4345c = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7409.62207, -46.3109131, 3117.40332 }
                boxMax: vec3 = { 7562.9668, 131.081787, 3270.74805 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    7486.29443, -46.3109131, 3194.07568, 1
                }
                name: string = "LevelProp_brush_SRU_D12"
            }
            0x9225c8d5 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4253.93604, -46.3118896, 4452.79785 }
                boxMax: vec3 = { 4498.00049, 167.294006, 4696.8623 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    4375.96826, -46.3118896, 4574.83008, 1
                }
                name: string = "LevelProp_brush_SRU_A3"
            }
            0xd093c49b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10338.6572, -46.3131027, 8376.96289 }
                boxMax: vec3 = { 10512.3252, 182.931793, 8550.63086 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    10425.4912, -46.3131027, 8463.79688, 1
                }
                name: string = "LevelProp_brush_SRU_B24"
            }
            0xf2588e9a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8158.03906, -46.3108673, 7959.86719 }
                boxMax: vec3 = { 8322.99219, 131.081833, 8124.81934 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.866878152, 0, -0.11102581, 0
                    0, 1, 0, 0
                    0.11102581, 0, 0.866878152, 0
                    8240.51562, -46.3108673, 8042.34326, 1
                }
                name: string = "LevelProp_brush_SRU_D30"
            }
            0x3b18c115 = GdsMapObject {
                type: u8 = 5
                boxMin: vec3 = { 11154.4873, -65.9958954, 6083.03418 }
                boxMax: vec3 = { 11564.4434, 624.970886, 6472.89355 }
                0xad304db5: string = "Characters/SRUAP_Turret_Chaos1/Skins/Skin10"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    -0.946017504, -0.0363752954, 0.32206741, 0
                    -0.0425141864, 0.99902308, -0.0120453155, 0
                    -0.321314663, -0.0250875149, -0.946639955, 0
                    11373.2226, -8, 6281.86182, 1
                }
                name: string = "Turret_T2_C_02"
            }
            0xdc008f58 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8071.00342, -46.6969185, 8018.95361 }
                boxMax: vec3 = { 8279.72461, 155.045959, 8227.6748 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.866878152, 0, -0.11102581, 0
                    0, 1, 0, 0
                    0.11102581, 0, 0.866878152, 0
                    8175.36426, -46.3109283, 8123.31445, 1
                }
                name: string = "LevelProp_brush_SRU_F28"
            }
            0x2cb7032e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8247.2207, -59.8548584, 9419.24805 }
                boxMax: vec3 = { 8400.60547, 83.143692, 9572.63281 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    8323.91308, -60.5196991, 9495.94043, 1
                }
                name: string = "LevelProp_brush_SRU_G52"
            }
            0x21f65e4b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 9429.15527, -49.1512451, 4649.05957 }
                boxMax: vec3 = { 9614.42676, 174.460785, 4834.3291 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.655681968, 0, 0.5778265, 0
                    0, 1, 0, 0
                    -0.5778265, 0, 0.655681968, 0
                    9521.79102, -46.3118057, 4741.69434, 1
                }
                name: string = "LevelProp_brush_SRU_C4"
            }
            0xf6d4e862 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7375.81055, -46.4315338, 6066.99414 }
                boxMax: vec3 = { 7534.50391, 135.846481, 6225.6875 }
                0xad304db5: string = "Characters/brush_SRU_E/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873620808, 0, 0.0243072212, 0
                    0, 1, 0, 0
                    -0.0243072212, 0, 0.873620808, 0
                    7455.15723, -46.3340149, 6146.34082, 1
                }
                name: string = "LevelProp_brush_SRU_E5"
            }
            0xef67d7c6 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10587.7803, -46.3110352, 4290.59424 }
                boxMax: vec3 = { 10799.7666, 182.933868, 4502.58057 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    10693.7734, -46.3110352, 4396.5874, 1
                }
                name: string = "LevelProp_brush_SRU_B4"
            }
            0xd49d50ec = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10449.4297, -49.1525421, 8392.61035 }
                boxMax: vec3 = { 10595.8496, 174.459473, 8539.03027 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    10522.6396, -46.3131027, 8465.82031, 1
                }
                name: string = "LevelProp_brush_SRU_C15"
            }
            0x3b059822 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7281.39844, -48.0078812, 5809.30176 }
                boxMax: vec3 = { 7413.89746, 94.9906693, 5941.80078 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    7347.64795, -48.6727219, 5875.55127, 1
                }
                name: string = "LevelProp_brush_SRU_G15"
            }
            0x03946c50 = GdsMapObject {
                type: u8 = 8
                boxMin: vec3 = { 2245.23779, -41.4796753, 7586.0293 }
                boxMax: vec3 = { 2339.85986, 242.246216, 7680.65137 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999969482, 0, -0.00780154252, 0
                    0, 1, 0, 0
                    0.00780154252, 0, 0.999969482, 0
                    2342.54907, -41.4799995, 7633.33984, 1
                }
                name: string = "__NAV_L001"
            }
            0x765a3eea = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8741.64844, -46.3124695, 3040.68286 }
                boxMax: vec3 = { 8901.78125, 182.932434, 3200.81421 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8821.71484, -46.3124695, 3120.74854, 1
                }
                name: string = "LevelProp_brush_SRU_B19"
            }
            0xcec7d2e8 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8065.1958, -65.5794373, 4417.69092 }
                boxMax: vec3 = { 8317.04883, 148.200302, 4669.54443 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.70795548, 0, 0.512449861, 0
                    0, 1, 0, 0
                    -0.512449861, 0, 0.70795548, 0
                    8191.12256, -65.4055939, 4543.61768, 1
                }
                name: string = "LevelProp_brush_SRU_I10"
            }
            0xe97a320e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7957.62891, -48.0090714, 8106.73926 }
                boxMax: vec3 = { 8101.19434, 94.9894791, 8250.30469 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.859185994, 0, -0.160011321, 0
                    0, 1, 0, 0
                    0.160011321, 0, 0.859185994, 0
                    8029.41162, -48.673912, 8178.52197, 1
                }
                name: string = "LevelProp_brush_SRU_G62"
            }
            0x428d5c2c = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4504.06836, -59.8552856, 8314.63281 }
                boxMax: vec3 = { 4657.45215, 83.1432648, 8468.01758 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    4580.76025, -60.5201263, 8391.3252, 1
                }
                name: string = "LevelProp_brush_SRU_G36"
            }
            0x468679e7 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 11036.8457, -46.3114014, 4611.21582 }
                boxMax: vec3 = { 11190.1894, 131.081299, 4764.56055 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    11113.5176, -46.3114014, 4687.88818, 1
                }
                name: string = "LevelProp_brush_SRU_D13"
            }
            0x5491c9df = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7483.33789, -46.3107529, 5801.83594 }
                boxMax: vec3 = { 7642.00293, 131.08194, 5960.50098 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    7562.67041, -46.3107529, 5881.16846, 1
                }
                name: string = "LevelProp_brush_SRU_D10"
            }
            0x15644d0a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6857.15381, -48.161438, 9348.29688 }
                boxMax: vec3 = { 7011.73096, 129.231262, 9502.875 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    6934.44238, -48.161438, 9425.58594, 1
                }
                name: string = "LevelProp_brush_SRU_D160"
            }
            0xce8471b5 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8169.16308, -46.3111992, 4591.7124 }
                boxMax: vec3 = { 8374.42676, 131.081497, 4796.97607 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.500265956, 0, 0.716616213, 0
                    0, 1, 0, 0
                    -0.716616213, 0, 0.500265956, 0
                    8271.79492, -46.3111992, 4694.34424, 1
                }
                name: string = "LevelProp_brush_SRU_D1"
            }
            0x6875b1fe = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4467.8706, -48.0087738, 4274.5415 }
                boxMax: vec3 = { 4635.48779, 94.9897766, 4442.15869 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    4551.6792, -48.6736145, 4358.3501, 1
                }
                name: string = "LevelProp_brush_SRU_G3"
            }
            0xd05d320d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10425.79, -46.6992149, 8354.60742 }
                boxMax: vec3 = { 10633.8604, 155.043671, 8562.67773 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.867318749, 0, -0.107529551, 0
                    0, 1, 0, 0
                    0.107529551, 0, 0.867318749, 0
                    10529.8252, -46.3132248, 8458.64258, 1
                }
                name: string = "LevelProp_brush_SRU_F17"
            }
            0xaf00a5d2 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 5480.97607, -46.698452, 10023.4277 }
                boxMax: vec3 = { 5713.38721, 155.044434, 10255.8398 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.836813867, 0, 0.252082944, 0
                    0, 1, 0, 0
                    -0.252082944, 0, 0.836813867, 0
                    5597.18164, -46.3124619, 10139.6338, 1
                }
                name: string = "LevelProp_brush_SRU_F9"
            }
            0x091dbff1 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6786.229, -46.6971703, 8042.31348 }
                boxMax: vec3 = { 6986.99463, 155.045715, 8243.0791 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    6886.61182, -46.3111801, 8142.69629, 1
                }
                name: string = "LevelProp_brush_SRU_F26"
            }
            0x8ad92e26 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7733.62451, -48.0083466, 6062.23291 }
                boxMax: vec3 = { 7860.10791, 94.9902039, 6188.71631 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873620808, 0, 0.0243072212, 0
                    0, 1, 0, 0
                    -0.0243072212, 0, 0.873620808, 0
                    7796.86621, -48.6731873, 6125.47461, 1
                }
                name: string = "LevelProp_brush_SRU_G13"
            }
            0x45f224ed = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6881.17285, -38.9926758, 9451.2666 }
                boxMax: vec3 = { 7035.75, 138.400024, 9605.84473 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    6958.46142, -38.9926758, 9528.55566, 1
                }
                name: string = "LevelProp_brush_SRU_D133"
            }
            0x2fcd7374 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8075.14258, -49.1503067, 7963.27881 }
                boxMax: vec3 = { 8222.02148, 174.461716, 8110.15771 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.866878152, 0, -0.11102581, 0
                    0, 1, 0, 0
                    0.11102581, 0, 0.866878152, 0
                    8148.58203, -46.3108673, 8036.71826, 1
                }
                name: string = "LevelProp_brush_SRU_C13"
            }
            0x1d712bbb = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 4356.60644, -43.4440308, 4261.71973 }
                boxMax: vec3 = { 4544.56543, 170.161865, 4449.67871 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.872871995, 0, 0.043525666, 0
                    0, 1, 0, 0
                    -0.043525666, 0, 0.872871995, 0
                    4450.58594, -43.4440308, 4355.69922, 1
                }
                name: string = "LevelProp_brush_SRU_A158"
            }
            0x1de162da = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8303.63965, -46.3119812, 3064.19897 }
                boxMax: vec3 = { 8455.26074, 131.080719, 3215.81958 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8379.4502, -46.3119812, 3140.00928, 1
                }
                name: string = "LevelProp_brush_SRU_D15"
            }
            0xaddab156 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7017.12598, -48.0075607, 7977.89648 }
                boxMax: vec3 = { 7179.55664, 94.9909897, 8140.32617 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.79900521, 0, 0.354113579, 0
                    0, 1, 0, 0
                    -0.354113579, 0, 0.79900521, 0
                    7098.34131, -48.6724014, 8059.11133, 1
                }
                name: string = "LevelProp_brush_SRU_G61"
            }
            0xb7aca3c7 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7270.08105, -59.8540039, 5998.65918 }
                boxMax: vec3 = { 7402.58008, 83.1445465, 6131.1582 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.871196568, 0, 0.0694329664, 0
                    0, 1, 0, 0
                    -0.0694329664, 0, 0.871196568, 0
                    7336.33057, -60.5188446, 6064.90869, 1
                }
                name: string = "LevelProp_brush_SRU_G16"
            }
            0xe0c8c106 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8025.16797, -59.8543015, 7936.22558 }
                boxMax: vec3 = { 8162.91797, 83.144249, 8073.97558 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.866878152, 0, -0.11102581, 0
                    0, 1, 0, 0
                    0.11102581, 0, 0.866878152, 0
                    8094.04297, -60.5191422, 8005.10058, 1
                }
                name: string = "LevelProp_brush_SRU_G50"
            }
            0xbf145ac7 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8467.05566, -46.432785, 3131.06982 }
                boxMax: vec3 = { 8625.91504, 135.84523, 3289.92969 }
                0xad304db5: string = "Characters/brush_SRU_E/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8546.48535, -46.3352661, 3210.49976, 1
                }
                name: string = "LevelProp_brush_SRU_E9"
            }
            0x2e6be57c = GdsMapObject {
                type: u8 = 1
                boxMin: vec3 = { 1726.22754, -41.4803467, 9216.6543 }
                boxMax: vec3 = { 1820.84961, 242.245544, 9311.27734 }
                0xad304db5: string = "Loadouts/SummonerBanners/Frames/Frame_1"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    1773.53857, -41.4803467, 9263.96582, 1
                }
                name: string = "__Spawn_T1"
            }
            0x2a3029fe = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 10588.0332, -112.752167, 4128.28906 }
                boxMax: vec3 = { 10804.4023, 94.0097046, 4344.65723 }
                0xad304db5: string = "Characters/brush_SRU_J/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762030244, 0, -0.427914649, 0
                    0, 1, 0, 0
                    0.427914649, 0, 0.762030244, 0
                    10696.2178, -112.5784, 4236.47314, 1
                }
                name: string = "LevelProp_brush_SRU_J9"
            }
            0x5f82b975 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6238.37305, -59.8544693, 2932.11401 }
                boxMax: vec3 = { 6366.42871, 83.1440811, 3060.16968 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    6302.40088, -60.51931, 2996.14185, 1
                }
                name: string = "LevelProp_brush_SRU_G20"
            }
            0x7442ed8f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7849.33301, -46.3119125, 9170.75293 }
                boxMax: vec3 = { 8034.20996, 131.08078, 9355.62793 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.842289746, 0, 0.253732502, 0
                    0, 1, 0, 0
                    -0.253732502, 0, 0.842289746, 0
                    7941.77148, -46.3119125, 9263.19043, 1
                }
                name: string = "LevelProp_brush_SRU_D35"
            }
            0x312692e2 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7926.84619, -59.8553467, 9330.25098 }
                boxMax: vec3 = { 8081.23389, 83.1432037, 9484.63965 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.842289746, 0, 0.253732502, 0
                    0, 1, 0, 0
                    -0.253732502, 0, 0.842289746, 0
                    8004.04004, -60.5201874, 9407.44531, 1
                }
                name: string = "LevelProp_brush_SRU_G55"
            }
            0x3ac3a3ee = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7003.14551, -63.9837036, 9358.90527 }
                boxMax: vec3 = { 7192.33398, 149.622192, 9548.09473 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.878583848, 0, 0.0438104868, 0
                    0, 1, 0, 0
                    -0.0438104868, 0, 0.878583848, 0
                    7097.73975, -63.9837036, 9453.5, 1
                }
                name: string = "LevelProp_brush_SRU_A25"
            }
            0xf9105054 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7918.41846, -41.477478, 9229.66016 }
                boxMax: vec3 = { 8082.74072, 187.767426, 9393.98242 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.878583848, 0, 0.0438104868, 0
                    0, 1, 0, 0
                    -0.0438104868, 0, 0.878583848, 0
                    8000.57959, -41.477478, 9311.82129, 1
                }
                name: string = "LevelProp_brush_SRU_B29"
            }
            0x5e4ff968 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7867.64307, -65.580307, 9230.5625 }
                boxMax: vec3 = { 8093.82764, 148.199432, 9456.74805 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.842289746, 0, 0.253732502, 0
                    0, 1, 0, 0
                    -0.253732502, 0, 0.842289746, 0
                    7980.73535, -65.4064636, 9343.65527, 1
                }
                name: string = "LevelProp_brush_SRU_I27"
            }
            0x2a3981a8 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7023.33301, -59.8555908, 9237.2793 }
                boxMax: vec3 = { 7177.7207, 83.1429596, 9391.66797 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.842289746, 0, 0.253732502, 0
                    0, 1, 0, 0
                    -0.253732502, 0, 0.842289746, 0
                    7100.52686, -60.5204315, 9314.47363, 1
                }
                name: string = "LevelProp_brush_SRU_G56"
            }
            0xc1e2ec61 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7114.32666, -42.5154419, 9287.24707 }
                boxMax: vec3 = { 7269.91553, 134.877258, 9442.83691 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.878583848, 0, 0.0438104868, 0
                    0, 1, 0, 0
                    -0.0438104868, 0, 0.878583848, 0
                    7192.12109, -42.5154419, 9365.04199, 1
                }
                name: string = "LevelProp_brush_SRU_D36"
            }
            0x4f1ea80c = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7162.896, -94.4795532, 9219.15234 }
                boxMax: vec3 = { 7352.08447, 119.126343, 9408.3418 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.878583848, 0, 0.0438104868, 0
                    0, 1, 0, 0
                    -0.0438104868, 0, 0.878583848, 0
                    7257.49023, -94.4795532, 9313.74707, 1
                }
                name: string = "LevelProp_brush_SRU_A40"
            }
            0x21f222c0 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8040.91894, -103.432129, 9261.10742 }
                boxMax: vec3 = { 8230.10742, 110.173767, 9450.29688 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.878583848, 0, 0.0438104868, 0
                    0, 1, 0, 0
                    -0.0438104868, 0, 0.878583848, 0
                    8135.51318, -103.432129, 9355.70215, 1
                }
                name: string = "LevelProp_brush_SRU_A42"
            }
            0xd97515b5 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8001.39014, -38.9920044, 9374.67285 }
                boxMax: vec3 = { 8156.979, 138.400696, 9530.2627 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.878583848, 0, 0.0438104868, 0
                    0, 1, 0, 0
                    -0.0438104868, 0, 0.878583848, 0
                    8079.18457, -38.9920044, 9452.46777, 1
                }
                name: string = "LevelProp_brush_SRU_D40"
            }
            0x160784e7 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7155.31104, -48.1608276, 9182.00684 }
                boxMax: vec3 = { 7310.8999, 129.231873, 9337.59668 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.878583848, 0, 0.0438104868, 0
                    0, 1, 0, 0
                    -0.0438104868, 0, 0.878583848, 0
                    7233.10547, -48.1608276, 9259.80176, 1
                }
                name: string = "LevelProp_brush_SRU_D41"
            }
            0x5dbe5ef2 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7119.39941, -43.7536926, 9236.19434 }
                boxMax: vec3 = { 7274.98828, 133.639008, 9391.78418 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.878583968, 0, 0.0438105464, 0
                    0, 1, 0, 0
                    -0.0438105464, 0, 0.878583968, 0
                    7197.19385, -43.7536926, 9313.98926, 1
                }
                name: string = "LevelProp_brush_SRU_D42"
            }
            0xb4fc342c = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8088.95752, -59.8551025, 9380.10547 }
                boxMax: vec3 = { 8243.34473, 83.1434479, 9534.49414 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.842289746, 0, 0.253732502, 0
                    0, 1, 0, 0
                    -0.253732502, 0, 0.842289746, 0
                    8166.15137, -60.5199432, 9457.2998, 1
                }
                name: string = "LevelProp_brush_SRU_G57"
            }
            0xe59ae1e4 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8015.60352, -50.6290512, 9248.43945 }
                boxMax: vec3 = { 8154.14453, 172.982971, 9386.98047 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.878583848, 0, 0.0438104868, 0
                    0, 1, 0, 0
                    -0.0438104868, 0, 0.878583848, 0
                    8084.87402, -47.7896118, 9317.70996, 1
                }
                name: string = "LevelProp_brush_SRU_C18"
            }
            0xf18e5ca5 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8311.82129, -46.6965981, 2963.01367 }
                boxMax: vec3 = { 8567.12012, 155.04628, 3218.31396 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.442454994, 0, 0.753682196, 0
                    0, 1, 0, 0
                    -0.753682196, 0, 0.442454994, 0
                    8439.4707, -46.3106079, 3090.66382, 1
                }
                name: string = "LevelProp_brush_SRU_F29"
            }
            0xaf609dc8 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6664.26318, -46.3110352, 3073.2439 }
                boxMax: vec3 = { 6877.35205, 182.933868, 3286.33325 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.442454994, 0, 0.753682196, 0
                    0, 1, 0, 0
                    -0.753682196, 0, 0.442454994, 0
                    6770.80762, -46.3110352, 3179.78857, 1
                }
                name: string = "LevelProp_brush_SRU_B31"
            }
            0xd3b7da6d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6260.55127, -48.0081024, 2865.93799 }
                boxMax: vec3 = { 6418.10693, 94.990448, 3023.49414 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.822188079, 0, 0.296327591, 0
                    0, 1, 0, 0
                    -0.296327591, 0, 0.822188079, 0
                    6339.3291, -48.6729431, 2944.71606, 1
                }
                name: string = "LevelProp_brush_SRU_G58"
            }
            0x15b7262d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7503.24707, -46.310791, 3113.48975 }
                boxMax: vec3 = { 7656.5918, 131.081909, 3266.83398 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    7579.91943, -46.310791, 3190.16187, 1
                }
                name: string = "LevelProp_brush_SRU_D43"
            }
            0x863765c7 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7524.53662, -46.3110352, 3091.5542 }
                boxMax: vec3 = { 7710.99658, 167.294861, 3278.01367 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    7617.7666, -46.3110352, 3184.78394, 1
                }
                name: string = "LevelProp_brush_SRU_A43"
            }
            0x6f450a4b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7443.91455, -49.1502304, 3028.01855 }
                boxMax: vec3 = { 7580.45752, 174.461792, 3164.56104 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873222172, 0, -0.035865128, 0
                    0, 1, 0, 0
                    0.035865128, 0, 0.873222172, 0
                    7512.18604, -46.310791, 3096.28979, 1
                }
                name: string = "LevelProp_brush_SRU_C20"
            }
            0xfa358c67 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8241.71191, -65.5793686, 2948.24512 }
                boxMax: vec3 = { 8488.55762, 148.200378, 3195.08984 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.442454994, 0, 0.753682196, 0
                    0, 1, 0, 0
                    -0.753682196, 0, 0.442454994, 0
                    8365.13476, -65.4055252, 3071.66748, 1
                }
                name: string = "LevelProp_brush_SRU_I28"
            }
            0x98812c55 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6706.97656, -46.3114014, 3024.52271 }
                boxMax: vec3 = { 6952.31152, 167.294495, 3269.85815 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.442454994, 0, 0.753682196, 0
                    0, 1, 0, 0
                    -0.753682196, 0, 0.442454994, 0
                    6829.64404, -46.3114014, 3147.19043, 1
                }
                name: string = "LevelProp_brush_SRU_A44"
            }
            0xf1f5b6c4 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7424.63818, -48.0083466, 3115.06689 }
                boxMax: vec3 = { 7582.19385, 94.9902039, 3272.62305 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.822188079, 0, 0.296327591, 0
                    0, 1, 0, 0
                    -0.296327591, 0, 0.822188079, 0
                    7503.41602, -48.6731873, 3193.84497, 1
                }
                name: string = "LevelProp_brush_SRU_G59"
            }
            0xe9b7782f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7541.51172, -46.3110962, 3069.16699 }
                boxMax: vec3 = { 7754.60058, 182.933807, 3282.25635 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.442454994, 0, 0.753682196, 0
                    0, 1, 0, 0
                    -0.753682196, 0, 0.442454994, 0
                    7648.05615, -46.3110962, 3175.71167, 1
                }
                name: string = "LevelProp_brush_SRU_B34"
            }
            0x9ec8890b = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7365.84082, -48.0080414, 2997.59814 }
                boxMax: vec3 = { 7534.33105, 94.990509, 3166.08838 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.442454994, 0, 0.753682196, 0
                    0, 1, 0, 0
                    -0.753682196, 0, 0.442454994, 0
                    7450.08594, -48.6728821, 3081.84326, 1
                }
                name: string = "LevelProp_brush_SRU_G63"
            }
            0xc3ff2513 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6379.77344, -46.6972694, 3051.44897 }
                boxMax: vec3 = { 6618.50586, 155.045609, 3290.18237 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.822188079, 0, 0.296327591, 0
                    0, 1, 0, 0
                    -0.296327591, 0, 0.822188079, 0
                    6499.13965, -46.3112793, 3170.81567, 1
                }
                name: string = "LevelProp_brush_SRU_F30"
            }
            0xda469079 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6317.24805, -59.8543472, 2913.44995 }
                boxMax: vec3 = { 6474.80371, 83.1442032, 3071.0061 }
                0xad304db5: string = "Characters/brush_SRU_G/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.822188079, 0, 0.296327591, 0
                    0, 1, 0, 0
                    -0.296327591, 0, 0.822188079, 0
                    6396.02588, -60.5191879, 2992.22803, 1
                }
                name: string = "LevelProp_brush_SRU_G64"
            }
            0x003c16e1 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6353.38721, -46.4313507, 3084.37305 }
                boxMax: vec3 = { 6551.06592, 135.846664, 3282.05176 }
                0xad304db5: string = "Characters/brush_SRU_E/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.822188079, 0, 0.296327591, 0
                    0, 1, 0, 0
                    -0.296327591, 0, 0.822188079, 0
                    6452.22656, -46.3338318, 3183.2124, 1
                }
                name: string = "LevelProp_brush_SRU_E17"
            }
            0xb532dc4a = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6567.2041, -65.5799179, 3031.19263 }
                boxMax: vec3 = { 6820.03516, 148.199829, 3284.02319 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.694166541, 0, 0.530976534, 0
                    0, 1, 0, 0
                    -0.530976534, 0, 0.694166541, 0
                    6693.61963, -65.4060745, 3157.60791, 1
                }
                name: string = "LevelProp_brush_SRU_I31"
            }
            0x14042885 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6472.229, -43.1336212, 2971.76807 }
                boxMax: vec3 = { 6689.72412, 163.62825, 3189.2627 }
                0xad304db5: string = "Characters/brush_SRU_J/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.442454994, 0, 0.753682196, 0
                    0, 1, 0, 0
                    -0.753682196, 0, 0.442454994, 0
                    6580.97656, -42.9598541, 3080.51538, 1
                }
                name: string = "LevelProp_brush_SRU_J16"
            }
            0x225423cb = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8734.39258, -46.3124695, 3114.96142 }
                boxMax: vec3 = { 8918.75586, 167.293427, 3299.3252 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8826.57422, -46.3124695, 3207.14331, 1
                }
                name: string = "LevelProp_brush_SRU_A45"
            }
            0x2ca7d27d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8538.6416, -46.3123474, 2940.14355 }
                boxMax: vec3 = { 8723.00488, 167.293549, 3124.50732 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8630.82324, -46.3123474, 3032.32544, 1
                }
                name: string = "LevelProp_brush_SRU_A46"
            }
            0xcbc06aa9 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7699.09277, -43.1349335, 3027.01294 }
                boxMax: vec3 = { 7862.53418, 163.626938, 3190.45532 }
                0xad304db5: string = "Characters/brush_SRU_J/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    7780.81348, -42.9611664, 3108.73413, 1
                }
                name: string = "LevelProp_brush_SRU_J19"
            }
            0x2bd72e02 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8416.45117, -65.5810471, 2900.10986 }
                boxMax: vec3 = { 8601.94922, 148.1987, 3085.60791 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8509.2002, -65.4072037, 2992.85889, 1
                }
                name: string = "LevelProp_brush_SRU_I32"
            }
            0xd53fdad7 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7613.95654, -46.6986427, 3117.0498 }
                boxMax: vec3 = { 7805.80908, 155.044235, 3308.90186 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    7709.88281, -46.3126526, 3212.97583, 1
                }
                name: string = "LevelProp_brush_SRU_F34"
            }
            0xc8bf1ed5 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8272.08203, -46.3124695, 3059.32397 }
                boxMax: vec3 = { 8456.44531, 167.293427, 3243.68774 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8364.26367, -46.3124695, 3151.50586, 1
                }
                name: string = "LevelProp_brush_SRU_A47"
            }
            0x8eef183d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7565.95117, -46.3124695, 3007.94482 }
                boxMax: vec3 = { 7726.08301, 182.932434, 3168.07617 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    7646.01709, -46.3124695, 3088.0105, 1
                }
                name: string = "LevelProp_brush_SRU_B35"
            }
            0xc68e52d8 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8598.46387, -46.3125916, 2899.69409 }
                boxMax: vec3 = { 8758.59668, 182.932312, 3059.82544 }
                0xad304db5: string = "Characters/brush_SRU_B/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    8678.53027, -46.3125916, 2979.75976, 1
                }
                name: string = "LevelProp_brush_SRU_B36"
            }
            0x33214447 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7626.16016, -46.3125916, 3056.52588 }
                boxMax: vec3 = { 7810.52441, 167.293304, 3240.88965 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    7718.34228, -46.3125916, 3148.70776, 1
                }
                name: string = "LevelProp_brush_SRU_A48"
            }
            0x1dd76eb2 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7527.43066, -46.6984596, 3038.6206 }
                boxMax: vec3 = { 7719.2832, 155.044418, 3230.47266 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873591781, 0, 0.0252772421, 0
                    0, 1, 0, 0
                    -0.0252772421, 0, 0.873591781, 0
                    7623.35693, -46.3124695, 3134.54663, 1
                }
                name: string = "LevelProp_brush_SRU_F35"
            }
            0xdae36bf9 = MapLocator {
                0xad304db5: string = "Characters/SLIME_NexusMinionBlue/Skins/Skin12"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.944649637, 0, -0.328086317, 0
                    0, 1, 0, 0
                    0.328086317, 0, -0.944649637, 0
                    1810.05273, -41.4776001, 8009.73291, 1
                }
                name: string = "NB_NexusMinion_Order"
            }
            0xa5a1d0b8 = MapLocator {
                0xad304db5: string = "Characters/SLIME_NexusMinionBlue/Skins/Skin13"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.835312188, 8.18645489e-08, 0.54977572, 0
                    1.33309584e-07, 0.999999881, 5.364112e-08, 0
                    -0.54977566, 1.18097461e-07, -0.835312188, 0
                    13329.9473, -41.4770012, 8009.73291, 1
                }
                name: string = "NB_NexusMinion_Chaos"
            }
            0xea400706 = MapLocator {
                0xad304db5: string = "Characters/SRU_MurkwolfMini/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.675276756, 0, -0.374238729, 0
                    0, 1, 0, 0
                    0.374238729, 0, -0.675276756, 0
                    4051.95996, -41.4783936, 9581.55078, 1
                }
                name: string = "OrderMurkwolfMini2"
            }
            0xb6cec84c = MapLocator {
                0xad304db5: string = "Characters/SRU_MurkwolfMini/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.675276756, 0, -0.374238729, 0
                    0, 1, 0, 0
                    0.374238729, 0, -0.675276756, 0
                    3831.92236, -41.4785156, 9436.43848, 1
                }
                name: string = "OrderMurkwolfMini1"
            }
            0xb2322390 = MapLocator {
                0xad304db5: string = "Characters/SRU_Murkwolf/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.619117022, 0, -0.461245984, 0
                    0, 1, 0, 0
                    0.461245984, 0, -0.619117022, 0
                    4036.23828, -41.4786377, 9381.45801, 1
                }
                name: string = "OrderMurkwolf"
            }
            0x5322cbe6 = MapLocator {
                0xad304db5: string = "Characters/SRU_Gromp/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.322145134, 0, -0.946690977, 0
                    0, 1, 0, 0
                    0.946690977, 0, -0.322145134, 0
                    4839.90137, -41.4775696, 8786.06445, 1
                }
                name: string = "OrderGromp"
            }
            0xd45c106a = MapLocator {
                0xad304db5: string = "Characters/SRU_RazorbeakMini/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.856316507, 0, 0.51645422, 0
                    0, 1, 0, 0
                    -0.51645422, 0, -0.856316507, 0
                    5862.3418, -41.4762039, 8893.46387, 1
                }
                name: string = "OrderRaptorMini5"
            }
            0x36bf9fb9 = MapLocator {
                0xad304db5: string = "Characters/SRU_RazorbeakMini/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.856316507, 0, 0.51645422, 0
                    0, 1, 0, 0
                    -0.51645422, 0, -0.856316507, 0
                    5832.09766, -43.752449, 8768.33887, 1
                }
                name: string = "OrderRaptorMini3"
            }
            0x20fe0bba = MapLocator {
                0xad304db5: string = "Characters/SRU_Razorbeak/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.862633586, 0.000177616428, 0.505832076, 0
                    0.000741859316, 0.999999285, 0.000914010743, 0
                    -0.50583148, 0.00116370933, -0.862633049, 0
                    5658.53125, -41.4772034, 8908.63867, 1
                }
                name: string = "OrderRaptor"
            }
            0x3a6b0602 = MapLocator {
                0xad304db5: string = "Characters/SRU_RazorbeakMini/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.862633586, 0.000177616428, 0.505832076, 0
                    0.000741859316, 0.999999285, 0.000914010743, 0
                    -0.50583148, 0.00116370933, -0.862633049, 0
                    5802.5166, -41.4762039, 9025.24414, 1
                }
                name: string = "OrderRaptorMini4"
            }
            0x97c18a39 = MapLocator {
                0xad304db5: string = "Characters/SRU_RazorbeakMini/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.853307784, 0, 0.521410167, 0
                    0, 1, 0, 0
                    -0.521410167, 0, -0.853307784, 0
                    5717.75195, -41.4757156, 8686.07226, 1
                }
                name: string = "OrderRaptorMini2"
            }
            0x9cf1adb6 = MapLocator {
                0xad304db5: string = "Characters/SRU_RazorbeakMini/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.853307724, 0, 0.521410286, 0
                    0, 1, 0, 0
                    -0.521410286, 0, -0.853307724, 0
                    5592.88574, -0.000244140625, 8755.87109, 1
                }
                name: string = "OrderRaptorMini1"
            }
            0x2b3f3f28 = MapLocator {
                0xad304db5: string = "Characters/SLIME_RiftHerald/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.999736369, 0, 0.023013683, 0
                    -0, 1, 0, 0
                    -0.023013683, 0, -0.999736369, 0
                    7567.1416, -43.7500305, 7975.6582, 1
                }
                name: string = "RiftHerald"
            }
            0xcfe662e1 = MapLocator {
                0xad304db5: string = "Characters/SLIME_RiftHerald_Relic/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    0.999971151, 0, -0.00780031085, 0
                    0, 1, 0, 0
                    0.00780031085, 0, 0.999971151, 0
                    7599.89551, 10.7557449, 7375.77197, 1
                }
                name: string = "RiftHeraldShrineLocation"
            }
            0x7ee56613 = MapLocator {
                0xad304db5: string = "Characters/SRU_RazorbeakMini/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.650932908, 0, -0.759136617, 0
                    0, 1, 0, 0
                    0.759136617, 0, -0.650932908, 0
                    9388.20215, -41.4728241, 9023.2334, 1
                }
                name: string = "ChaosRaptorMini1"
            }
            0xe3ab2fce = MapLocator {
                0xad304db5: string = "Characters/SRU_RazorbeakMini/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.650932908, 0, -0.759136617, 0
                    0, 1, 0, 0
                    0.759136617, 0, -0.650932908, 0
                    9589.33008, -41.4728241, 8784.70996, 1
                }
                name: string = "ChaosRaptorMini5"
            }
            0xb011c9d3 = MapLocator {
                0xad304db5: string = "Characters/SRU_Razorbeak/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.650932908, 0, -0.759136617, 0
                    0, 1, 0, 0
                    0.759136617, 0, -0.650932908, 0
                    9551.92188, -41.4737015, 8927.1123, 1
                }
                name: string = "ChaosRaptor"
            }
            0x7c247497 = MapLocator {
                0xad304db5: string = "Characters/SRU_RazorbeakMini/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.64959538, 0, -0.760281324, 0
                    0, 1, 0, 0
                    0.760281324, 0, -0.64959538, 0
                    9354.03613, -41.4739456, 8898.99316, 1
                }
                name: string = "ChaosRaptorMini3"
            }
            0xab51d1db = MapLocator {
                0xad304db5: string = "Characters/SRU_RazorbeakMini/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.64959538, 0, -0.760281324, 0
                    0, 1, 0, 0
                    0.760281324, 0, -0.64959538, 0
                    9497.99121, -41.4738846, 8726.06055, 1
                }
                name: string = "ChaosRaptorMini4"
            }
            0xe7d8a4b4 = MapLocator {
                0xad304db5: string = "Characters/SRU_RazorbeakMini/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.64959538, 0, -0.760281324, 0
                    0, 1, 0, 0
                    0.760281324, 0, -0.64959538, 0
                    9387.58008, -41.4738846, 8776.70605, 1
                }
                name: string = "ChaosRaptorMini2"
            }
            0xa45f5790 = MapLocator {
                0xad304db5: string = "Characters/SRU_Gromp/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.648809671, 0, 0.760952413, 0
                    0, 1, 0, 0
                    -0.760952413, 0, -0.648809671, 0
                    10337.0713, -41.4743958, 8807.80176, 1
                }
                name: string = "ChaosGromp"
            }
            0x41db6497 = MapLocator {
                0xad304db5: string = "Characters/SRU_Murkwolf/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.399379671, 0, 0.660719037, 0
                    0, 1, 0, 0
                    -0.660719037, 0, -0.399379671, 0
                    11116.2188, -43.7524719, 9395.80664, 1
                }
                name: string = "ChaosMurkwolf"
            }
            0x2c7c1dbd = MapLocator {
                0xad304db5: string = "Characters/SRU_MurkwolfMini/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.663464904, 0, 0.394800872, 0
                    0, 1, 0, 0
                    -0.394800872, 0, -0.663464904, 0
                    11104.7578, -41.4768677, 9581.38965, 1
                }
                name: string = "ChaosMurkwolfMini1"
            }
            0x457969d1 = MapLocator {
                0xad304db5: string = "Characters/SRU_Blue/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.843984425, 0, -0.536371648, 0
                    0, 1, 0, 0
                    0.536371648, 0, -0.843984425, 0
                    9279.16797, -41.4767456, 5690.19726, 1
                }
                name: string = "ChaosBlueBuff"
            }
            0xfb51ab04 = MapLocator {
                0xad304db5: string = "Characters/SRU_Blue/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.974555016, 0, 0.224158317, 0
                    0, 1, 0, 0
                    -0.224158317, 0, -0.974555016, 0
                    5883.1123, -41.4780884, 5698.61719, 1
                }
                name: string = "OrderBlueBuff"
            }
            0x0b5451a5 = MapLocator {
                0xad304db5: string = "Characters/SRU_Krug/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.997940242, -8.72427108e-08, -0.0641491339, 0
                    -8.18146759e-08, 0.999999881, -8.72427108e-08, 0
                    0.064149119, -8.18146759e-08, -0.997940242, 0
                    5958.60986, -6.10351562e-05, 10195.1875, 1
                }
                name: string = "OrderKrug"
            }
            0x4291a1bf = MapLocator {
                0xad304db5: string = "Characters/SRU_KrugMini/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.997940242, -8.72427108e-08, -0.0641491339, 0
                    -8.18146759e-08, 0.999999881, -8.72427108e-08, 0
                    0.064149119, -8.18146759e-08, -0.997940242, 0
                    6193.01807, 0, 10173.4766, 1
                }
                name: string = "OrderKrugMini"
            }
            0x252a7124 = MapLocator {
                0xad304db5: string = "Characters/SRU_Krug/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.997940242, -8.72427108e-08, -0.0641491339, 0
                    -8.18146759e-08, 0.999999881, -8.72427108e-08, 0
                    0.064149119, -8.18146759e-08, -0.997940242, 0
                    9242.50293, 0, 10198.9014, 1
                }
                name: string = "ChaosKrug"
            }
            0x46cf9123 = MapLocator {
                0xad304db5: string = "Characters/SRU_KrugMini/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.997940242, -8.72427108e-08, -0.0641491339, 0
                    -8.18146759e-08, 0.999999881, -8.72427108e-08, 0
                    0.064149119, -8.18146759e-08, -0.997940242, 0
                    9017.94434, 0.000244140625, 10160.0869, 1
                }
                name: string = "ChaosKrugMini"
            }
            0xfd441046 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Red"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11476.9726, -50.1358337, 8620.39844, 1
                }
                name: string = "ChaosBaseGate"
            }
            0x2b1a656a = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Blue"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3628.4043, -50.1375427, 8582.90332, 1
                }
                name: string = "OrderBaseGate"
            }
            0x888c16ac = MapLocator {
                0xad304db5: string = "Characters/SRU_MurkwolfMini/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.399379671, 0, 0.660719037, 0
                    0, 1, 0, 0
                    -0.660719037, 0, -0.399379671, 0
                    11310.3369, -43.7522278, 9367.58594, 1
                }
                name: string = "ChaosMurkwolfMini2"
            }
            0x164c59f2 = MapLocator {
                0xad304db5: string = "Characters/SRU_Red/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.999317527, -8.51982449e-08, -0.0369730145, 0
                    -8.11832876e-08, 0.999999881, -1.10095755e-07, 0
                    0.0369730443, -1.07018735e-07, -0.999317527, 0
                    7626.22558, 6.10351562e-05, 9953.2041, 1
                }
                name: string = "RedBuff"
            }
            0xdfb5a9de = MapLocator {
                0xad304db5: string = "Characters/SRU_Red/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.292366296, -2.55594745e-08, 0.0672455058, 0
                    -3.21056213e-08, 0.299999982, -2.55594745e-08, 0
                    -0.0672454983, -3.21056213e-08, -0.292366296, 0
                    7584.09326, -0.000877929735, 10086.2119, 1
                }
                name: string = "RedCampCenterpoint"
            }
            0x3ccb1d54 = MapLocator {
                0xad304db5: string = "Characters/SRU_Red/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.396943063, 3.47018663e-08, -0.0493574552, 0
                    3.06541459e-08, 0.399999946, 3.47018663e-08, 0
                    0.0493574515, 3.06541459e-08, -0.396943063, 0
                    7644.33984, -0.000366210938, 9785.45508, 1
                }
                name: string = "RedBuffPickup"
            }
            0x22c207ad = MapLocator {
                0xad304db5: string = "Characters/SRU_Blue/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.389821708, -3.40792994e-08, 0.0896606743, 0
                    -4.28074927e-08, 0.399999946, -3.40792994e-08, 0
                    -0.0896606669, -4.28074962e-08, -0.389821708, 0
                    5862.58984, -41.4780006, 5609.41406, 1
                }
                name: string = "OrderBlueBuffPickup"
            }
            0x2063db82 = MapLocator {
                0xad304db5: string = "Characters/SRU_Blue/Skins/Skin0"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.337592691, -2.95132914e-08, -0.214548752, 0
                    -1.62126614e-08, 0.399999946, -2.95132914e-08, 0
                    0.214548707, -1.62126632e-08, -0.337592691, 0
                    9342.25195, -41.4770012, 5629.78076, 1
                }
                name: string = "ChaosBlueBuffPickup"
            }
            0x479b20c0 = GdsMapObject {
                type: u8 = 5
                boxMin: vec3 = { 3411.47217, -534.769348, 8695.31348 }
                boxMax: vec3 = { 3857.51196, 467.502563, 9136.14453 }
                0xad304db5: string = "Characters/SRUAP_Turret_Chaos1/Skins/Skin11"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.664737582, -0.000952546485, -0.747081399, 0
                    -0.060005907, 0.996700227, -0.0546628088, 0
                    0.744668424, 0.0811652243, 0.66248703, 0
                    3635.10132, -43.752594, 8916.28418, 1
                }
                name: string = "Turret_T1_R_01"
            }
            0x67617ff0 = GdsMapObject {
                type: u8 = 5
                boxMin: vec3 = { 11282.4854, -72.2050018, 8708.58789 }
                boxMax: vec3 = { 11757.3428, 634.099915, 9136.08008 }
                0xad304db5: string = "Characters/SRUAP_Turret_Chaos1/Skins/Skin10"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    -0.804306567, -0.0607726537, 0.591098487, 0
                    -0.0828784779, 0.996506214, -0.0103187161, 0
                    -0.588406205, -0.0572887547, -0.806533277, 0
                    11546.7334, -8, 8925.6748, 1
                }
                name: string = "Turret_T2_R_01"
            }
            0x4b7101b2 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Blue"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2756.56909, 0, 6893.41504, 1
                }
                name: string = "EventStart_Order"
            }
            0x000e9466 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Red"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12135.8203, -0.000244140625, 6622.74609, 1
                }
                name: string = "EventStart_Chaos"
            }
            0x004aa435 = MapParticle {
                system: link = "Maps/Particles/NexusBlitz/SRUAP_Order_BaseDoor_Shield_Bottom"
                transform: mtx44 = {
                    0.98480773, 0, -0.173648179, 0
                    0, 1, 0, 0
                    0.173648179, 0, 0.98480773, 0
                    3854.08228, 6.10351562e-05, 8505.71289, 1
                }
                name: string = "SRUAP_Order_BaseDoor_Shield_Bottom1"
            }
            0xacbba966 = MapParticle {
                system: link = "Maps/Particles/NexusBlitz/SRUAP_Order_BaseDoor_Bottom"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3826.78223, 0, 8581.97852, 1
                }
                name: string = "SRUAP_Order_BaseDoor_Bottom1"
            }
            0x9acf73ae = MapParticle {
                system: link = "Maps/Particles/NexusBlitz/SRUAP_Chaos_BaseDoor_Bottom"
                transform: mtx44 = {
                    0.99999994, 0, 0, 0
                    0, 0.99999994, 0, 0
                    0, 0, 0.999999881, 0
                    11494.456, 0, 8616.625, 1
                }
                name: string = "SRUAP_Chaos_BaseDoor_Bottom1"
            }
            0x1fa7a7c1 = MapParticle {
                system: link = "Maps/Particles/NexusBlitz/SRUAP_Chaos_BaseDoor_Shield_Bottom"
                transform: mtx44 = {
                    0.0871558711, 0, -0.99619472, 0
                    0, 0.99999994, 0, 0
                    0.996194661, 0, 0.0871558636, 0
                    11577.6611, 0, 8627.07715, 1
                }
                name: string = "SRUAP_Chaos_BaseDoor_Shield_Bottom1"
            }
            0x639338d3 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Blue"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2588.47705, 0.000122070312, 7050.42627, 1
                }
                name: string = "NexusFacing_Order"
            }
            0x16801f60 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Red"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12338.0107, -0.00048828125, 6792.771, 1
                }
                name: string = "NexusFacing_Chaos"
            }
            0x536cf7ad = MapLocator {
                0xad304db5: string = "Characters/NexusBlitz_Shopkeeper/Skins/Skin2"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.857589364, -7.49728457e-08, 0.514334738, 0
                    -1.32387342e-07, 0.999999881, -7.49728457e-08, 0
                    -0.514334619, -1.32387328e-07, -0.857589364, 0
                    2383.9956, 45.2731628, 9083.74023, 1
                }
                name: string = "NB_OrderShopkeeper"
            }
            0xe94f2855 = MapLocator {
                0xad304db5: string = "Characters/NexusBlitz_Shopkeeper/Skins/Skin1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.988970935, -0.07545688, 0.127449214, 0
                    -0.0702023804, 0.996506572, 0.0452351272, 0
                    -0.130417198, 0.035788998, -0.990813315, 0
                    12836.1191, 15.5410805, 9064.6709, 1
                }
                name: string = "NB_ChaosShopkeeper"
            }
            0x7f5abcde = MapLocator {
                0xad304db5: string = "Characters/NexusBlitz_Shopkeeper/Skins/Skin2"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.343035758, 2.99891383e-08, 0.205733895, 0
                    5.29549382e-08, 0.399999946, 2.99891383e-08, 0
                    -0.205733851, 5.29549311e-08, -0.343035758, 0
                    2382.35205, 0, 8977.7793, 1
                }
                name: string = "NB_OrderShopkeeperFacing"
            }
            0xa8910ba0 = MapLocator {
                0xad304db5: string = "Characters/NexusBlitz_Shopkeeper/Skins/Skin1"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -0.361409903, -2.99891383e-08, -0.171414316, 0
                    -4.40284254e-09, 0.399999946, -6.06975235e-08, 0
                    0.171414346, -5.29549311e-08, -0.361409843, 0
                    12838.7139, 0.000946044922, 8940.58594, 1
                }
                name: string = "NB_ChaosShopkeeperFacing"
            }
            0x1fd026d1 = MapGroup {
                members: list2[string] = {
                    "8d8bee8a-3680-4711-a34e-7f5ad2d0e73a"
                    "e062db22-a20d-4f69-a44d-c72b66caa86e"
                    "de576e27-557f-4a7f-8e8f-840e99c554a4"
                    "3c6b59f7-2743-4d7e-ba21-1770c062019c"
                    "67eb1dc7-f3e1-45ca-9f92-d854c7966559"
                    "45c09678-27a4-4004-a062-9fce23d34059"
                    "15db54a7-3628-4602-8406-9cb69fe9f9bd"
                    "b1b6afaf-6994-454b-8a65-170a97e5c4a8"
                    "eb94efd5-7002-42bf-a4fb-266ec60ff322"
                    "35d0cc4c-b2db-4e5d-8bc9-6290d358571e"
                    "67cc7710-6243-4161-afeb-39523b8b2482"
                    "a727df7e-ba8e-4817-ba4d-7acb364b6d77"
                    "445a961f-3387-47fc-bd72-8cd3a8272601"
                    "28154762-d753-4043-893f-066582989d6b"
                    "37a9dd88-0d91-4d55-a8fb-098a7d1d3cb6"
                    "d3e749ec-1110-4ec4-bd72-d8892604c4be"
                    "abe17d13-4dac-4d34-b8f7-9ddadb47244c"
                    "9da58082-2c30-47b9-bdbf-655eab07c7cb"
                    "822059e2-bd59-40a5-bba9-bd4e899cf951"
                    "a06c6b7f-f0f6-4d7b-ade0-38b6afb9a509"
                    "4e471790-f21d-4d0b-98ab-dc311cc447aa"
                    "c72d1aee-12bd-4094-a165-13de241f1ac6"
                    "1ce84b76-6e35-4505-bad3-0b22a1d7ae41"
                }
                transform: mtx44 = {
                    0.594998062, 0, 0.803727567, 0
                    0, 1, 0, 0
                    -0.803727567, 0, 0.594998062, 0
                    8099.74219, -46.3113403, 4734.45703, 1
                }
                name: string = "group133"
            }
            0xabd77404 = MapGroup {
                members: list2[string] = {
                    "32df7496-2b21-4bb0-b122-37d8b58ddc22"
                    "bb5b638f-a357-42f0-b65a-27d2f465f855"
                    "02f918e5-4d3a-4419-9974-380e52c4f40e"
                    "946ea860-a131-4868-95d9-e3dee7c900fe"
                    "c3560bda-6a0f-4a60-8c72-b9958dd27f0a"
                    "5f9f98ff-6280-4aa1-8c1e-d4dd363ca355"
                    "8033bf89-cef1-40d4-b12a-4da56283f1e8"
                    "736bfef3-df54-4f83-97cc-2c72904724ea"
                    "0800dbf5-6dd7-4acc-9830-219d660a616d"
                    "485abb6f-c540-4f62-b8f1-b4484a401d09"
                    "605e9891-b08e-4b1f-96dc-3d7fdc5e0c5c"
                    "628cae29-a936-4777-9922-e43160cbf4d0"
                    "dc8b4c69-f896-4818-bebe-61c68bf8a71c"
                    "fde177a2-031c-47e3-bf4b-bf4fc79fb08f"
                    "a4a3f5d4-b443-4ce5-bc80-8c6e1f3e188a"
                    "152852bc-c9a3-420f-a60d-e1331688e0aa"
                    "ee85eb6e-44b2-4b5f-85fa-09fb1b52799c"
                    "03de2950-8a47-489e-b40d-78c912102958"
                    "0dc2a339-7950-42b1-83d4-6995db1b24eb"
                    "fd59c3c5-9dba-45d5-9afc-34c96e2c01ba"
                    "523501d5-a0ce-45c8-9534-d7bd38f0ad87"
                    "7185ec92-cc16-4a7b-a782-ebb8a249661b"
                }
                name: string = "group135"
            }
            0x71b79454 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6987.57617, -46.3113022, 4442.53906 }
                boxMax: vec3 = { 7188.9375, 131.08139, 4643.90039 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.757008016, 0, 0.436742902, 0
                    0, 1, 0, 0
                    -0.436742902, 0, 0.757008016, 0
                    7088.25684, -46.3113022, 4543.21973, 1
                }
                name: string = "LevelProp_brush_SRU_D44"
            }
            0xfe0e8a1d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7082.76855, -46.311058, 4408.75 }
                boxMax: vec3 = { 7286.99805, 131.081635, 4612.97949 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.481201142, 0, -0.729555011, 0
                    0, 1, 0, 0
                    0.729555011, 0, 0.481201142, 0
                    7184.8833, -46.311058, 4510.86475, 1
                }
                name: string = "LevelProp_brush_SRU_D45"
            }
            0x96dbae17 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6860.15186, -65.5800781, 4630.56006 }
                boxMax: vec3 = { 7110.54541, 148.199661, 4880.95361 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.724394143, 0, 0.488935888, 0
                    0, 1, 0, 0
                    -0.488935888, 0, 0.724394143, 0
                    6985.34863, -65.4062347, 4755.75684, 1
                }
                name: string = "LevelProp_brush_SRU_I33"
            }
            0xd7bb6d7e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7141.27392, -46.6974754, 4420.92139 }
                boxMax: vec3 = { 7399.69385, 155.04541, 4679.34131 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.481201142, 0, -0.729555011, 0
                    0, 1, 0, 0
                    0.729555011, 0, 0.481201142, 0
                    7270.48389, -46.3114853, 4550.13135, 1
                }
                name: string = "LevelProp_brush_SRU_F36"
            }
            0x144c2cc9 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6855.13184, -46.3108978, 4563.23682 }
                boxMax: vec3 = { 7105.76758, 167.294998, 4813.87256 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.518269658, 0, -0.703705966, 0
                    0, 1, 0, 0
                    0.703705966, 0, 0.518269658, 0
                    6980.44971, -46.3108978, 4688.55469, 1
                }
                name: string = "LevelProp_brush_SRU_A27"
            }
            0xdea29cd8 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7031.45264, -46.3106537, 4478.36182 }
                boxMax: vec3 = { 7283.69971, 167.295242, 4730.60889 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.67639643, 0, -0.553437829, 0
                    0, 1, 0, 0
                    0.553437829, 0, 0.67639643, 0
                    7157.57617, -46.3106537, 4604.48535, 1
                }
                name: string = "LevelProp_brush_SRU_A49"
            }
            0x89345173 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6992.46387, -49.150032, 4528.20312 }
                boxMax: vec3 = { 7176.00195, 174.46199, 4711.74121 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.518269658, 0, -0.703705966, 0
                    0, 1, 0, 0
                    0.703705966, 0, 0.518269658, 0
                    7084.23291, -46.3105927, 4619.97217, 1
                }
                name: string = "LevelProp_brush_SRU_C22"
            }
            0x073120c6 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6931.94873, -49.150032, 4514.33594 }
                boxMax: vec3 = { 7110.61768, 174.46199, 4693.00488 }
                0xad304db5: string = "Characters/brush_SRU_C/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.762535214, 0, -0.427019358, 0
                    0, 1, 0, 0
                    0.427019358, 0, 0.762535214, 0
                    7021.2832, -46.3105927, 4603.67041, 1
                }
                name: string = "LevelProp_brush_SRU_C23"
            }
            0xbf72e963 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7052.78516, -46.311058, 4398.55469 }
                boxMax: vec3 = { 7240.76855, 131.081635, 4586.53808 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.824441671, 0, -0.29000172, 0
                    0, 1, 0, 0
                    0.29000172, 0, 0.824441671, 0
                    7146.77686, -46.311058, 4492.54639, 1
                }
                name: string = "LevelProp_brush_SRU_D46"
            }
            0xe45f1724 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7099.13379, -46.311058, 4334.54883 }
                boxMax: vec3 = { 7304.11719, 131.081635, 4539.53223 }
                0xad304db5: string = "Characters/brush_SRU_D/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.720351696, 0, 0.494872212, 0
                    0, 1, 0, 0
                    -0.494872212, 0, 0.720351696, 0
                    7201.62549, -46.311058, 4437.04053, 1
                }
                name: string = "LevelProp_brush_SRU_D47"
            }
            0xcffe797f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8062.0498, -65.5794373, 4552.14844 }
                boxMax: vec3 = { 8243.67871, 148.200302, 4733.77734 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.873937964, 0, 0.00618121028, 0
                    0, 1, 0, 0
                    -0.00618121028, 0, 0.873937964, 0
                    8152.86426, -65.4055939, 4642.96289, 1
                }
                name: string = "LevelProp_brush_SRU_I36"
            }
            0xd0284ed8 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7877.0625, -65.5794373, 4315.78174 }
                boxMax: vec3 = { 8117.45508, 148.200302, 4556.17432 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.375862002, 0, -0.789007902, 0
                    0, 1, 0, 0
                    0.789007902, 0, 0.375862002, 0
                    7997.25879, -65.4055939, 4435.97803, 1
                }
                name: string = "LevelProp_brush_SRU_I37"
            }
            0x3fac2b2d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7783.09766, -46.311039, 4425.96387 }
                boxMax: vec3 = { 8018.5791, 167.294861, 4661.44531 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.802895308, 0, 0.345202416, 0
                    0, 1, 0, 0
                    -0.345202416, 0, 0.802895308, 0
                    7900.83838, -46.311039, 4543.70459, 1
                }
                name: string = "LevelProp_brush_SRU_A50"
            }
            0x42ac6611 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7871.57226, -46.696785, 4333.18896 }
                boxMax: vec3 = { 8128.56641, 155.046097, 4590.1831 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.462554663, 0, 0.741517842, 0
                    0, 1, 0, 0
                    -0.741517842, 0, 0.462554663, 0
                    8000.06934, -46.3107948, 4461.68604, 1
                }
                name: string = "LevelProp_brush_SRU_F38"
            }
            0x611872c4 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8003.37695, -46.3107948, 4373.97314 }
                boxMax: vec3 = { 8250.33984, 167.295105, 4620.93604 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.462554663, 0, 0.741517842, 0
                    0, 1, 0, 0
                    -0.741517842, 0, 0.462554663, 0
                    8126.8584, -46.3107948, 4497.45459, 1
                }
                name: string = "LevelProp_brush_SRU_A51"
            }
            0xd9f374c7 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7256.06689, -46.6974754, 4364.19287 }
                boxMax: vec3 = { 7518.70459, 155.04541, 4626.83057 }
                0xad304db5: string = "Characters/brush_SRU_F/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    -0.673238099, 0, -0.557275116, 0
                    0, 1, 0, 0
                    0.557275116, 0, -0.673238099, 0
                    7387.38574, -46.3114853, 4495.51172, 1
                }
                name: string = "LevelProp_brush_SRU_F40"
            }
            0xdac1dbf8 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7215.20166, -46.3106537, 4428.21045 }
                boxMax: vec3 = { 7465.8374, 167.295242, 4678.84619 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.518269658, 0, -0.703705966, 0
                    0, 1, 0, 0
                    0.703705966, 0, 0.518269658, 0
                    7340.51953, -46.3106537, 4553.52832, 1
                }
                name: string = "LevelProp_brush_SRU_A53"
            }
            0xeb37b384 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7192.11035, -46.3108978, 4316.97705 }
                boxMax: vec3 = { 7431.87695, 167.294998, 4556.74365 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.383818209, 0, 0.785168529, 0
                    0, 1, 0, 0
                    -0.785168529, 0, 0.383818209, 0
                    7311.99365, -46.3108978, 4436.86035, 1
                }
                name: string = "LevelProp_brush_SRU_A54"
            }
            0xf851213c = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6873.74365, -46.3106537, 4734.50146 }
                boxMax: vec3 = { 7090.74658, 167.295242, 4951.50439 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.848470271, 0, -0.209532201, 0
                    0, 1, 0, 0
                    0.209532201, 0, 0.848470271, 0
                    6982.24512, -46.3106537, 4843.00293, 1
                }
                name: string = "LevelProp_brush_SRU_A52"
            }
            0x34004e5d = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7812.46045, -65.5800781, 4378.15283 }
                boxMax: vec3 = { 8039.7749, 148.199661, 4605.46728 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.831067145, 0, 0.27042973, 0
                    0, 1, 0, 0
                    -0.27042973, 0, 0.831067145, 0
                    7926.11768, -65.4062347, 4491.81006, 1
                }
                name: string = "LevelProp_brush_SRU_I39"
            }
            0x47ea3194 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 7789.49365, -46.311039, 4304.50439 }
                boxMax: vec3 = { 8024.9751, 167.294861, 4539.98584 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.802895308, 0, 0.345202416, 0
                    0, 1, 0, 0
                    -0.345202416, 0, 0.802895308, 0
                    7907.23438, -46.311039, 4422.24512, 1
                }
                name: string = "LevelProp_brush_SRU_A55"
            }
            0x3a665ab7 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8124.47412, -46.3107948, 4658.66553 }
                boxMax: vec3 = { 8374.67773, 167.295105, 4908.86963 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.709333718, 0, -0.510540307, 0
                    0, 1, 0, 0
                    0.510540307, 0, 0.709333718, 0
                    8249.57617, -46.3107948, 4783.76758, 1
                }
                name: string = "LevelProp_brush_SRU_A56"
            }
            0x426e8374 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8154.32129, -65.5794373, 4720.50928 }
                boxMax: vec3 = { 8406.1748, 148.200302, 4972.36279 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.70795548, 0, 0.512449861, 0
                    0, 1, 0, 0
                    -0.512449861, 0, 0.70795548, 0
                    8280.24805, -65.4055939, 4846.43604, 1
                }
                name: string = "LevelProp_brush_SRU_I38"
            }
            0x4061ed18 = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6920.98682, -46.3106537, 4618.61279 }
                boxMax: vec3 = { 7156.40283, 167.295242, 4854.02881 }
                0xad304db5: string = "Characters/brush_SRU_A/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.344637185, 0, -0.803138077, 0
                    0, 1, 0, 0
                    0.803138077, 0, 0.344637185, 0
                    7038.69482, -46.3106537, 4736.3208, 1
                }
                name: string = "LevelProp_brush_SRU_A12"
            }
            0x98b8622f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 8832.59375, -65.5811691, 2934.17651 }
                boxMax: vec3 = { 9051.63672, 148.198578, 3153.21997 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    -0.214089558, 0, 0.847329736, 0
                    0, 1, 0, 0
                    -0.847329736, 0, -0.214089558, 0
                    8942.11523, -65.4073257, 3043.69824, 1
                }
                name: string = "LevelProp_brush_SRU_I34"
            }
            0xc7a0394f = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 6776.59717, -65.5799179, 2945.4458 }
                boxMax: vec3 = { 7029.42822, 148.199829, 3198.27637 }
                0xad304db5: string = "Characters/brush_SRU_I/Skins/Skin0"
                sceneLayer: string = "Spawn Locators"
                transform: mtx44 = {
                    0.694166541, 0, 0.530976534, 0
                    0, 1, 0, 0
                    -0.530976534, 0, 0.694166541, 0
                    6903.0127, -65.4060745, 3071.86108, 1
                }
                name: string = "LevelProp_brush_SRU_I35"
            }
            0xe0155546 = MapGroup {
                members: list2[string] = {
                    "33b8d454-7540-41d5-a4ad-ca0c41344b4b"
                    "e18ae53e-f4ff-41bb-bbea-425f7f378d9f"
                    "0051b831-048c-492e-bdae-b557b38af4ef"
                    "7fd76737-7072-4736-bf78-c8d8ff2270e1"
                }
                transform: mtx44 = {
                    0.775512993, -0.0845313221, 0.625647008, 0
                    0, 0.990995705, 0.133893684, 0
                    -0.631331682, -0.103836291, 0.768530071, 0
                    1365.04089, -1344.31177, 5853.6831, 1
                }
                name: string = "group144"
            }
        }
        path: string = "Maps/MapGeometry/Map21/Chunks/MapObjects"
    }
    "Maps/MapGeometry/Map21/Chunks/OldMap_Lights_Particles" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xf46502dd = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Motes_Ground"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8519.89648, -29.480011, 6838.45898, 1
                }
                name: string = "Odyssey_Motes_Ground16"
            }
            0x31083527 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4140.7373, -29.4798889, 9027.90234, 1
                }
                name: string = "Odyssey_Ground_Wind23"
            }
            0x668cd631 = MapPointLight {
                type: link = 0xf695f759
                radiusScale: f32 = 0.513264656
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3593.13013, 240.30246, 8667.83203, 1
                }
                name: string = "nb_orange_01_5"
            }
            0xa638466b = MapParticle {
                system: link = "Maps/Particles/SR/Sru_torch_fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4706.45166, 179.999069, 7261.97803, 1
                }
                name: string = "Sru_torch_fire3"
            }
            0x08cb7bc1 = MapPointLight {
                type: link = 0x6a8afea7
                radiusScale: f32 = 1.20000005
                intensityScale: f32 = 0.699999988
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9226.13965, 381.020172, 5466.94824, 1
                }
                name: string = "nb_blue_01_3"
            }
            0xcead5b09 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_wispfly"
                transform: mtx44 = {
                    -0.45431447, 0, 0.890841663, 0
                    0, 1, 0, 0
                    -0.890841663, 0, -0.45431447, 0
                    9662.18164, 101.963028, 4739.98242, 1
                }
                name: string = "Odyssey_wispfly1"
            }
            0x3bf7aaa5 = MapPointLight {
                type: link = 0xecf322d5
                radiusScale: f32 = 1.20000005
                intensityScale: f32 = 0.699999988
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5890.57568, 489.870636, 8172.55762, 1
                }
                name: string = "nb_purple_01_1"
            }
            0x7674fad2 = MapPointLight {
                type: link = 0xecf322d5
                radiusScale: f32 = 1.20000005
                intensityScale: f32 = 0.699999988
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6068.93896, 439.92868, 10145.5322, 1
                }
                name: string = "nb_purple_01_3"
            }
            0x25761f89 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Motes_Ground"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9112.58887, -29.4809875, 9306.35352, 1
                }
                name: string = "Odyssey_Motes_Ground8"
            }
            0x8e227cc2 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7765.02148, -29.4802551, 7370.24854, 1
                }
                name: string = "Odyssey_Ground_Wind19"
            }
            0xbb831c24 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Motes_Ground"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    13531.7266, -29.4809875, 7352.24658, 1
                }
                name: string = "Odyssey_Motes_Ground14"
            }
            0xc14c10e0 = MapPointLight {
                type: link = 0x97e9e6de
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    876.41333, 818.200439, 8249.46094, 1
                }
                name: string = "nb_tan_fill3"
            }
            0x01315310 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10254.7695, -29.4811096, 6354.13672, 1
                }
                name: string = "Odyssey_Ground_Wind27"
            }
            0x4af1862e = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4459.85791, -29.48172, 5699.08691, 1
                }
                name: string = "Odyssey_Ground_Wind30"
            }
            0xfbfb1c0c = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Motes_Ground"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7472.65478, -29.480011, 4376.18652, 1
                }
                name: string = "Odyssey_Motes_Ground3"
            }
            0x7164c721 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10809.6885, -29.4813538, 5085.4209, 1
                }
                name: string = "Odyssey_Ground_Wind26"
            }
            0x80e9ccef = MapPointLight {
                type: link = 0x97e9e6de
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5826.96191, 818.200928, 3797.51367, 1
                }
                name: string = "nb_tan_fill10"
            }
            0x42f30f8a = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Motes_Ground"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5726.72656, -29.480011, 3819.30835, 1
                }
                name: string = "Odyssey_Motes_Ground1"
            }
            0x8f5a049a = MapPointLight {
                type: link = 0x97e9e6de
                radiusScale: f32 = 0.762556434
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12078.873, 624.926025, 8183.80859, 1
                }
                name: string = "nb_tan_fill16"
            }
            0xce905438 = MapPointLight {
                type: link = 0xf695f759
                radiusScale: f32 = 0.513264656
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5357.94824, 233.783844, 8924.98926, 1
                }
                name: string = "nb_orange_01_6"
            }
            0x311c07f4 = MapPointLight {
                type: link = 0xc3b20305
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7549.35352, 296.294403, 9353.26172, 1
                }
                name: string = "nb_Herald1"
            }
            0x6f7247d5 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_wispfly"
                transform: mtx44 = {
                    -0.45431447, 0, 0.890841663, 0
                    0, 1, 0, 0
                    -0.890841663, 0, -0.45431447, 0
                    8506.31055, 101.962784, 7611.13965, 1
                }
                name: string = "Odyssey_wispfly4"
            }
            0x5d013227 = MapParticle {
                system: link = "Maps/Particles/SR/Sru_torch_fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4708.64892, 135.98526, 5604.56152, 1
                }
                name: string = "Sru_torch_fire10"
            }
            0xc5612f6d = MapPointLight {
                type: link = 0x97e9e6de
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11343.4443, 818.199463, 6387.30469, 1
                }
                name: string = "nb_tan_fill6"
            }
            0xca6fc3e0 = MapPointLight {
                type: link = 0x97e9e6de
                radiusScale: f32 = 0.762556434
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3021.14209, 624.926025, 8183.80859, 1
                }
                name: string = "nb_tan_fill15"
            }
            0x696ddc2b = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Motes_Ground"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1463.59155, -29.4812317, 7308.99023, 1
                }
                name: string = "Odyssey_Motes_Ground11"
            }
            0x0723533d = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6587.81592, -29.4797058, 5654.98242, 1
                }
                name: string = "Odyssey_Ground_Wind16"
            }
            0x4158a4d0 = MapParticle {
                system: link = "Maps/Particles/SR/Sru_torch_fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7889.52881, 140.396362, 5134.8457, 1
                }
                name: string = "Sru_torch_fire5"
            }
            0x484ab108 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Motes_Ground"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6380.5957, -29.480011, 6838.45898, 1
                }
                name: string = "Odyssey_Motes_Ground15"
            }
            0xb319c05a = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9489.80371, -29.4812317, 6319.99902, 1
                }
                name: string = "Odyssey_Ground_Wind8"
            }
            0x4a171779 = MapParticle {
                system: link = "Maps/Particles/SR/Sru_torch_fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10238.8076, 139.117218, 5488.40478, 1
                }
                name: string = "Sru_torch_fire9"
            }
            0x768bcf9b = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7538.25439, -29.4802551, 6525.0581, 1
                }
                name: string = "Odyssey_Ground_Wind1"
            }
            0x6dc4b717 = MapPointLight {
                type: link = 0x97e9e6de
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    14485.5957, 818.198975, 8487.72461, 1
                }
                name: string = "nb_tan_fill8"
            }
            0xc73ca2f5 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Motes_Ground"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12464.9688, -29.4809875, 8288.01758, 1
                }
                name: string = "Odyssey_Motes_Ground9"
            }
            0x3ac94568 = MapParticle {
                system: link = "Maps/Particles/SR/Sru_torch_fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5357.1206, 195.861298, 8925.01465, 1
                }
                name: string = "Sru_torch_fire1"
            }
            0x434331ba = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7929.55664, -29.4792175, 3410.63428, 1
                }
                name: string = "Odyssey_Ground_Wind17"
            }
            0xd8bd87e6 = MapPointLight {
                type: link = 0x97e9e6de
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2125.36572, 818.200928, 7470.99121, 1
                }
                name: string = "nb_tan_fill2"
            }
            0xee08e4c7 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Motes_Ground"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5809.7666, -29.4804993, 9404.0332, 1
                }
                name: string = "Odyssey_Motes_Ground7"
            }
            0x27dafa8e = MapParticle {
                system: link = "Maps/Particles/SR/Sru_braziers_fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6917.65918, 130.28302, 8888.21387, 1
                }
                name: string = "Sru_braziers_fire2"
            }
            0x8df78a8e = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11030.0928, -29.4812317, 6074.08691, 1
                }
                name: string = "Odyssey_Ground_Wind7"
            }
            0x1e7cfb9b = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Motes_Ground"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10535.6719, -29.4797668, 6329.62598, 1
                }
                name: string = "Odyssey_Motes_Ground6"
            }
            0x74ca47bb = MapPointLight {
                type: link = 0x97e9e6de
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6082.56104, 818.199951, 6860.28808, 1
                }
                name: string = "nb_tan_fill4"
            }
            0xf35fb9cd = MapPointLight {
                type: link = 0xf695f759
                radiusScale: f32 = 0.513264656
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7886.87988, 190.781372, 5135.15039, 1
                }
                name: string = "nb_orange_01_12"
            }
            0xe84434a4 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12196.3779, -29.4802551, 8200.60644, 1
                }
                name: string = "Odyssey_Ground_Wind9"
            }
            0xfc3a1913 = MapPointLight {
                type: link = 0xfbe666a7
                radiusScale: f32 = 1.20000005
                intensityScale: f32 = 0.699999988
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10410.1172, 406.686737, 7517.64014, 1
                }
                name: string = "nb_teal_01_4"
            }
            0x1dbd4ffb = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5360.82373, -29.4814758, 3762.28027, 1
                }
                name: string = "Odyssey_Ground_Wind29"
            }
            0x6274bf2a = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9943.95117, -29.48172, 4045.60596, 1
                }
                name: string = "Odyssey_Ground_Wind6"
            }
            0xf147d424 = MapPointLight {
                type: link = 0xf695f759
                radiusScale: f32 = 0.513264656
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5905.04688, 169.686554, 7462.14941, 1
                }
                name: string = "nb_orange_01_7"
            }
            0x6842ea44 = MapParticle {
                system: link = "Maps/Particles/SR/SLIME_turret_AOE"
                transform: mtx44 = {
                    0.600000024, 0, 0, 0
                    0, 0.600000024, 0, 0
                    0, 0, 0.600000024, 0
                    9769.51758, -23.8470001, 9237.18359, 1
                }
                name: string = "SLIME_turret_AOE11"
            }
            0x88f31df8 = MapPointLight {
                type: link = 0x97e9e6de
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9390.4209, 818.199951, 3865.28516, 1
                }
                name: string = "nb_tan_fill9"
            }
            0x68887c85 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_wispfly"
                transform: mtx44 = {
                    -0.45431447, 0, 0.890841663, 0
                    0, 1, 0, 0
                    -0.890841663, 0, -0.45431447, 0
                    5079.60596, 101.962784, 4569.34766, 1
                }
                name: string = "Odyssey_wispfly2"
            }
            0x39c70267 = MapPointLight {
                type: link = 0x62439fa8
                radiusScale: f32 = 1.32361937
                intensityScale: f32 = 0.800000012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7500.85644, 321.032745, 7683.81055, 1
                }
                name: string = "nb_red_01_1"
            }
            0x37a1bfaf = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5361.38184, -29.4802551, 6306.7417, 1
                }
                name: string = "Odyssey_Ground_Wind14"
            }
            0x470730a2 = MapPointLight {
                type: link = 0x97e9e6de
                radiusScale: f32 = 0.600000024
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7436.64111, 482.459564, 10428.6455, 1
                }
                name: string = "nb_tan_fill11"
            }
            0x586ca651 = MapPointLight {
                type: link = 0xecf322d5
                radiusScale: f32 = 1.20000005
                intensityScale: f32 = 0.699999988
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4667.42139, 489.870392, 7529.16357, 1
                }
                name: string = "nb_purple_01_4"
            }
            0x9e249b23 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    13921.3887, -29.4802551, 7555.51758, 1
                }
                name: string = "Odyssey_Ground_Wind10"
            }
            0xc23653d5 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7766.97558, -29.4792786, 8632.86035, 1
                }
                name: string = "Odyssey_Ground_Wind13"
            }
            0x27a9132b = MapPointLight {
                type: link = 0x6a8afea7
                radiusScale: f32 = 1.20000005
                intensityScale: f32 = 0.699999988
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5846.54248, 410.394196, 5519.55127, 1
                }
                name: string = "nb_blue_01_2"
            }
            0x9c49ae4d = MapParticle {
                system: link = "Maps/Particles/SR/Sru_torch_fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9090.01855, 103.544479, 7386.24854, 1
                }
                name: string = "Sru_torch_fire6"
            }
            0xb907ef67 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Motes_Ground"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2451.96094, -29.4809875, 8302.50586, 1
                }
                name: string = "Odyssey_Motes_Ground10"
            }
            0xa07bed4f = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8479.92773, -29.480011, 5720.90234, 1
                }
                name: string = "Odyssey_Ground_Wind2"
            }
            0xec1053b3 = MapParticle {
                system: link = "Maps/Particles/SR/Sru_torch_fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9649.24609, 181.575699, 8903.16406, 1
                }
                name: string = "Sru_torch_fire7"
            }
            0xcc9fbc3b = MapPointLight {
                type: link = 0xfbe666a7
                radiusScale: f32 = 1.20000005
                intensityScale: f32 = 0.699999988
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9074.89551, 421.507294, 8261.14062, 1
                }
                name: string = "nb_teal_01_3"
            }
            0x96bf1956 = MapPointLight {
                type: link = 0xf695f759
                radiusScale: f32 = 0.513264656
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4708.03613, 210.193054, 7264.75976, 1
                }
                name: string = "nb_orange_01_14"
            }
            0x88e2acc8 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9493.7793, -29.4808655, 8080.86328, 1
                }
                name: string = "Odyssey_Ground_Wind24"
            }
            0xdfcb5b4d = MapPointLight {
                type: link = 0xfbe666a7
                radiusScale: f32 = 1.20000005
                intensityScale: f32 = 0.699999988
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9116.52734, 421.50827, 10030.957, 1
                }
                name: string = "nb_teal_01_1"
            }
            0x2ddb348b = MapPointLight {
                type: link = 0x97e9e6de
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12975.0898, 818.198486, 7652.05908, 1
                }
                name: string = "nb_tan_fill7"
            }
            0x1480f56a = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6842.79394, -29.4803772, 7989.30029, 1
                }
                name: string = "Odyssey_Ground_Wind20"
            }
            0xcaf181fd = MapParticle {
                system: link = "Maps/Particles/SR/Sru_torch_fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3586.08252, 195.127777, 8662.70312, 1
                }
                name: string = "Sru_torch_fire2"
            }
            0x4c1a370a = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Motes_Ground"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2837.66211, -29.4809875, 6632.01318, 1
                }
                name: string = "Odyssey_Motes_Ground12"
            }
            0xe91922d5 = MapPointLight {
                type: link = 0x97e9e6de
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9081.83496, 818.200928, 6822.28516, 1
                }
                name: string = "nb_tan_fill5"
            }
            0xe2c2267f = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11950.334, -29.4811096, 6583.4834, 1
                }
                name: string = "Odyssey_Ground_Wind25"
            }
            0x2c954a7f = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6957.36816, -29.4794617, 3427.41382, 1
                }
                name: string = "Odyssey_Ground_Wind18"
            }
            0x25b03f17 = MapPointLight {
                type: link = 0xecf322d5
                radiusScale: f32 = 1.20000005
                intensityScale: f32 = 0.699999988
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4782.46338, 439.92868, 8781.61816, 1
                }
                name: string = "nb_purple_01_2"
            }
            0x140a81f8 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4010.78857, -29.4804993, 5005.62842, 1
                }
                name: string = "Odyssey_Ground_Wind4"
            }
            0x335eeef1 = MapPointLight {
                type: link = 0xfbe666a7
                radiusScale: f32 = 1.20000005
                intensityScale: f32 = 0.699999988
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10234.123, 406.686249, 8728.87305, 1
                }
                name: string = "nb_teal_01_2"
            }
            0x29972160 = MapPointLight {
                type: link = 0xf695f759
                radiusScale: f32 = 0.513264656
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4706.27783, 190.781311, 5607.51758, 1
                }
                name: string = "nb_orange_01_13"
            }
            0xcd95071d = MapParticle {
                system: link = "Maps/Particles/SR/Sru_torch_fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11391.2344, 195.197128, 8737.90039, 1
                }
                name: string = "Sru_torch_fire8"
            }
            0xe0a23085 = MapPointLight {
                type: link = 0x97e9e6de
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3682.38135, 818.199951, 6433.27637, 1
                }
                name: string = "nb_tan_fill1"
            }
            0xd0d133b6 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_wispfly"
                transform: mtx44 = {
                    -0.45431447, 0, 0.890841663, 0
                    0, 1, 0, 0
                    -0.890841663, 0, -0.45431447, 0
                    6968.02686, 101.962784, 5466.85352, 1
                }
                name: string = "Odyssey_wispfly3"
            }
            0x5a9b9b50 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6875.39502, -29.4802551, 4698.31982, 1
                }
                name: string = "Odyssey_Ground_Wind3"
            }
            0x681a1e54 = MapPointLight {
                type: link = 0xf695f759
                radiusScale: f32 = 0.513264656
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10241.0332, 174.22229, 5489.62744, 1
                }
                name: string = "nb_orange_01_11"
            }
            0x8bc0850a = MapParticle {
                system: link = "Maps/Particles/SR/Sru_torch_fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5906.87549, 135.985504, 7457.33203, 1
                }
                name: string = "Sru_torch_fire4"
            }
            0xcd27464a = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Motes_Ground"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9227.9834, -29.480011, 3807.15552, 1
                }
                name: string = "Odyssey_Motes_Ground2"
            }
            0x7d646ab5 = MapPointLight {
                type: link = 0xf695f759
                radiusScale: f32 = 0.513264656
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8090.24805, 330.401398, 8922.70605, 1
                }
                name: string = "nb_orange_01_2"
            }
            0x5a37589d = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4586.54785, -29.4815979, 4337.3042, 1
                }
                name: string = "Odyssey_Ground_Wind28"
            }
            0x43d749a8 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Godrays"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5676.76318, 97.5209961, 10679.3506, 1
                }
                name: string = "Odyssey_Godrays2"
            }
            0x211981ca = MapParticle {
                system: link = "Maps/Particles/Snowdown/Snow_StartOfGame_Square"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1116.60913, 18.2006531, 5524.11328, 1
                }
                name: string = "Snow_StartOfGame_Circle12"
            }
            0x75cb2a30 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8469.26367, -29.4812317, 4165.24316, 1
                }
                name: string = "Odyssey_Ground_Wind5"
            }
            0xa2191640 = MapParticle {
                system: link = "Maps/Particles/SR/Sru_braziers_fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8120.43018, 130.28302, 8937.40918, 1
                }
                name: string = "Sru_braziers_fire1"
            }
            0x0bcd5e81 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3027.55127, -29.4797668, 8144.23535, 1
                }
                name: string = "Odyssey_Ground_Wind12"
            }
            0x9446a7a5 = MapPointLight {
                type: link = 0x97e9e6de
                radiusScale: f32 = 0.394125342
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7546.3081, 239.044281, 6839.7998, 1
                }
                name: string = "nb_tan_fill12"
            }
            0xa5626551 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5879.7832, -29.4801331, 8974.96094, 1
                }
                name: string = "Odyssey_Ground_Wind21"
            }
            0xe6b8bf27 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9448.42578, -29.4802551, 8721.88281, 1
                }
                name: string = "Odyssey_Ground_Wind11"
            }
            0xbb4edbfd = MapPointLight {
                type: link = 0xf695f759
                radiusScale: f32 = 0.513264656
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6931.00879, 330.401398, 8922.70605, 1
                }
                name: string = "nb_orange_01_1"
            }
            0x1fcbb634 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1639.68848, -29.4802551, 8214.97266, 1
                }
                name: string = "Odyssey_Ground_Wind15"
            }
            0x5047690c = MapPointLight {
                type: link = 0x97e9e6de
                radiusScale: f32 = 1.07544458
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7546.3081, 695.455933, 5349.35547, 1
                }
                name: string = "nb_tan_fill14"
            }
            0x518007a5 = MapPointLight {
                type: link = 0x97e9e6de
                radiusScale: f32 = 0.394125342
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7546.3081, 231.081451, 3623.56348, 1
                }
                name: string = "nb_tan_fill13"
            }
            0x4b47dc8b = MapPointLight {
                type: link = 0xf695f759
                radiusScale: f32 = 0.513264656
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11391.6338, 231.631775, 8740.33203, 1
                }
                name: string = "nb_orange_01_9"
            }
            0x5f648425 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Godrays"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8687.32422, -0.266204834, 10730.0342, 1
                }
                name: string = "Odyssey_Godrays3"
            }
            0x4aabdb16 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Motes_Ground"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12264.1807, -29.4814758, 6895.4165, 1
                }
                name: string = "Odyssey_Motes_Ground13"
            }
            0x2cf80bea = MapPointLight {
                type: link = 0xf695f759
                radiusScale: f32 = 0.513264656
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9646.30957, 231.631775, 8902.33984, 1
                }
                name: string = "nb_orange_01_10"
            }
            0x15bb3b27 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Motes_Ground"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7473.14746, -29.480011, 6838.45898, 1
                }
                name: string = "Odyssey_Motes_Ground4"
            }
            0x4a898eae = MapPointLight {
                type: link = 0xf695f759
                radiusScale: f32 = 0.513264656
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9086.21484, 152.69104, 7386.47607, 1
                }
                name: string = "nb_orange_01_8"
            }
            0x65d54b19 = MapParticle {
                system: link = "Maps/Particles/SR/SLIME_turret_AOE"
                transform: mtx44 = {
                    0.600000024, 0, 0, 0
                    0, 0.600000024, 0, 0
                    0, 0, 0.600000024, 0
                    5218.22217, -23.8479996, 9209.34863, 1
                }
                name: string = "SLIME_turret_AOE12"
            }
            0x67a10767 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Motes_Ground"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4276.229, -29.4797668, 6456.88184, 1
                }
                name: string = "Odyssey_Motes_Ground5"
            }
            0x55cbc20f = MapPointLight {
                type: link = 0x6a8afea7
                radiusScale: f32 = 1.99999976
                intensityScale: f32 = 0.699999988
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7505.32226, 337.067108, 5001.02344, 1
                }
                name: string = "nb_blue_01_1"
            }
            0xa953ca44 = MapParticle {
                system: link = "Maps/Particles/Odyssey/Odyssey_Ground_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5166.48193, -29.4798889, 7096.98682, 1
                }
                name: string = "Odyssey_Ground_Wind22"
            }
        }
        path: string = "Maps/MapGeometry/Map21/Chunks/OldMap_Lights_Particles"
    }
    "Maps/MapGeometry/Map21/Materials/Ground_Blend" = StaticMaterialDef {
        name: string = "Maps/MapGeometry/Map21/Materials/Ground_Blend"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Bottom_Texture"
                textureName: string = "ASSETS/Shared/Materials/TerrainBlending/SRU_Ground_Stone_1024.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Middle_Texture"
                textureName: string = "ASSETS/Shared/Materials/TerrainBlending/SRU_Ground_Dirt_1024.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Top_Texture"
                textureName: string = "ASSETS/Shared/Materials/TerrainBlending/SRU_Ground_Grass_1024.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Extras_Texture"
                textureName: string = "ASSETS/Shared/Materials/TerrainBlending/Vines.dds"
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "MASK"
                textureName: string = "ASSETS/Shared/Materials/TerrainBlending/Noise3.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "WS_Multiplier"
                value: vec4 = { 0.00999999978, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "MASK_Intensity"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Red_Blend_Power"
                value: vec4 = { 4, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Green_Blend_Power"
                value: vec4 = { 4, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Blue_Blend_Power"
                value: vec4 = { 4, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bottom_Tiling"
                value: vec4 = { 0.100000001, 0.100000001, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Mid_Tiling"
                value: vec4 = { 0.0799999982, 0.0799999982, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Top_Tiling"
                value: vec4 = { 0.200000003, 0.200000003, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Extra_Tiling"
                value: vec4 = { 0.100000001, 0.100000001, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "OV_Low"
                value: vec4 = { 0.230000004, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "OV_High"
                value: vec4 = { 0.564999998, 0, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_TOP"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_EXTRAS"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_A_AS_OVERLAY"
            }
            StaticMaterialSwitchDef {
                name: string = "SHOW_RED_MASK"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "SHOW_GREEN_MASK"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "SHOW_BLUE_MASK"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "SHOW_PAINTED_A"
                on: bool = false
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/4TextureBlend_WorldProjected"
                    }
                }
            }
        }
        dynamicMaterial: pointer = DynamicMaterialDef {
            textures: list[embed] = {
                DynamicMaterialTextureSwapDef {
                    name: string = "Bottom_Texture"
                }
            }
        }
    }
    "Maps/MapGeometry/Map21/Base" = mapContainer {
        mapPath: string = "Maps/MapGeometry/Map21/Base"
        components: list[pointer] = {
            MapSunProperties {
                sunColor: vec4 = { 0.607843161, 0.698039234, 0.827450991, 1 }
                sunDirection: vec3 = { -0.210754275, 0.928618789, -0.305368155 }
                skyLightColor: vec4 = { 0.419607848, 0.529411793, 0.596078455, 1 }
                groundColor: vec4 = { 0.325490206, 0.325490206, 0.325490206, 1 }
                skyLightScale: f32 = 0.800000012
                lightMapColorScale: f32 = 2
                fogColor: vec4 = { 0.454901963, 0.478431374, 0.403921574, 1 }
                fogAlternateColor: vec4 = { 0, 0, 0, 1 }
                fogStartAndEnd: vec2 = { 0, -5000 }
            }
            MapBakeProperties {
                lightGridFileName: string = "ASSETS/Maps/Lightmaps/Maps/MapGeometry/Map21/Base/LightGrid.NexusBlitzSummer2020.dat"
            }
            MapTerrainPaint {
                0xc2e98f06: string = "ASSETS/Maps/TerrainPaint/Maps/MapGeometry/Map21/Base.png"
            }
        }
        boundsMax: vec2 = { 15000, 15000 }
        lowestWalkableHeight: f32 = -100
        chunks: map[hash,link] = {
            "Default" = "Maps/MapGeometry/Map21/Chunks/Default"
            "locators" = "Maps/MapGeometry/Map21/Chunks/Locators"
            "MapObjects" = "Maps/MapGeometry/Map21/Chunks/MapObjects"
            "OldMap_Meshes" = "Maps/MapGeometry/Map21/Chunks/OldMap_Meshes"
            "OldMap_Lights_Particles" = "Maps/MapGeometry/Map21/Chunks/OldMap_Lights_Particles"
        }
    }
    0x62439fa8 = MapPointLightType {
        lightColor: vec4 = { 0.776470602, 0, 0.0117647061, 1 }
        radius: f32 = 800
    }
    0x6a8afea7 = MapPointLightType {
        lightColor: vec4 = { 0.227450982, 0.227450982, 1, 1 }
        radius: f32 = 800
        castStaticShadows: bool = false
    }
    0x97e9e6de = MapPointLightType {
        lightColor: vec4 = { 0.776470602, 0.75686276, 0.678431392, 1 }
        radius: f32 = 1600
        castStaticShadows: bool = false
    }
    0xc3b20305 = MapPointLightType {
        lightColor: vec4 = { 0.776470602, 0, 0.713725507, 1 }
        radius: f32 = 1000
        castStaticShadows: bool = false
    }
    0xecf322d5 = MapPointLightType {
        lightColor: vec4 = { 0.270588249, 0.850980401, 0.109803922, 1 }
        radius: f32 = 1000
    }
    0xf695f759 = MapPointLightType {
        lightColor: vec4 = { 0.972549021, 0.329411775, 0.0274509806, 1 }
        radius: f32 = 808
    }
    0xfbe666a7 = MapPointLightType {
        lightColor: vec4 = { 0.694117665, 0.250980407, 0.866666675, 1 }
        radius: f32 = 1000
    }
}
