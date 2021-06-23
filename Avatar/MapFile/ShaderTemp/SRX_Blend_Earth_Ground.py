"Material_Name" = StaticMaterialDef {
        name: string = "Material_Name"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/SRX/Map_Name/Texture_Name"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Noise_Texture"
                textureName: string = "ASSETS/Shared/Materials/SRX_Mountain_Noise.dds"
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Decal_Texture"
                textureName: string = "ASSETS/Shared/Materials/black.dds"
                addressU: u32 = 1
                addressV: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "UV_Offset"
            }
            StaticMaterialShaderParamDef {
                name: string = "Decal_UV_Tile"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Translate"
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Rotation"
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Rotation_Center"
                value: vec4 = { 0.5, 0.5, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Decal_Transition_Factor"
                value: vec4 = { 5, 0, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "MASK_FX_IN_MAP_CENTER"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "ENABLE_GROUND_DECAL"
                on: bool = false
            }
        }
        shaderMacros: map[string,string] = {
            NOBAKEDLIGHTINGTEMP
            DISABLEDEPTHFOG
            PREMULTIPLIEDALPHA
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/SRX_Blend_Earth_Ground"
                        cullEnable: bool = false
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