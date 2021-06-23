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
                textureName: string = "ASSETS/Shared/Materials/SRX_Ocean_Noise.dds"
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Tint_Color"
                value: vec4 = { -0.0700000003, -0.0399999991, -0.0199999996, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Spec_Color"
                value: vec4 = { 0.486274511, 0.839215696, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Specular_Min_Max"
                value: vec4 = { 0.219999999, 0.620000005, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Specular_Intensity"
                value: vec4 = { 0.600000024, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Specular_Mask_Distance"
                value: vec4 = { 0.200000003, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Transition_Opacity"
                value: vec4 = { 1, 0, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "MASK_FX_IN_MAP_CENTER"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "ENABLE_TRANSITION_FADE"
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
                        shader: link = "Shaders/Environment/SRX_Blend_Ocean"
                        cullEnable: bool = false
                    }
                }
            }
        }
        childTechniques: list[embed] = {
            StaticMaterialChildTechniqueDef {
                name: string = "env_transition"
                parentName: string = "normal"
                shaderMacros: map[string,string] = {
                    "ENV_TRANSITION" = "1"
                }
            }
        }
    }