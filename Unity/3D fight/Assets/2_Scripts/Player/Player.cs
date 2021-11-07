using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{
    #region FunctionClass Reference

    [HideInInspector] public PlayerController _controller;
    [HideInInspector] public PlayerAnimator _animator;
    [HideInInspector] public PlayerCombat _combat;

    #endregion

    private void Awake()
    {
        _controller = GetComponent<PlayerController>();
        _animator = GetComponent<PlayerAnimator>();
        _combat = GetComponent<PlayerCombat>();
    }
}
