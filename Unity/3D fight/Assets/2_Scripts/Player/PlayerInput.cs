using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerInput : MonoBehaviour
{
    [HideInInspector] public Player player;
    public float inputX;
    public float inputY;
    
    private void Awake()
    {
        player = GetComponent<Player>();
    }

    private void Update()
    {
        inputX = Input.GetAxisRaw("Horizontal");
        inputY = Input.GetAxisRaw("Vertical");

        if (Input.GetMouseButtonDown(0))
        {
            player._combat.Attack();
        }

        if (Input.GetKeyDown(KeyCode.LeftShift))
        {
            player._controller.Roll();
        }
            
    }
}
