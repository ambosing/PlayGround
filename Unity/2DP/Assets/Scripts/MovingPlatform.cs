using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public enum TriggerType
{
    Always,
    PlayerOn,
    PlayerOff
}

public enum MoveDirection
{
    Horizontal,
    Vertical
}

public class MovingPlatform : PlatformBase 
{
    public MoveDirection direction;
    public Vector2 moveVector;
    public float moveDistance;
    public float moveSpeed;
    private Vector3 curDestination;

    //public TriggerType actionTriggerType;
    private Vector3 destination1Pos;
    private Vector3 destination2Pos;

    private void Awake()
    {
        switch (direction)
        {
            case MoveDirection.Horizontal:
                destination1Pos = transform.position - new Vector3(moveDistance, 0f, 0f);
                destination2Pos = transform.position + new Vector3(moveDistance, 0f, 0f);
                break;
            case MoveDirection.Vertical:
                destination1Pos = transform.position - new Vector3(0f, moveDistance, 0f);
                destination2Pos = transform.position + new Vector3(0f, moveDistance, 0f);
                break;
        }
        curDestination = destination1Pos;
    }

    private void Update()
    {
        Move();
        //switch (actionTriggerType)    
        //{
        //    case TriggerType.Always:
        //        break;
        //    case TriggerType.PlayerOn:
        //        break;
        //    case TriggerType.PlayerOff:
        //        break;
        //}
    }

    private void Move()
    {
        if (Vector3.Distance(transform.position, destination1Pos) < 0.1f)
        {
            curDestination = destination2Pos;
        }
        else if (Vector3.Distance(transform.position, destination2Pos) < 0.1f)
        {
            curDestination = destination1Pos;
        }
        transform.position = Vector3.Lerp(transform.position, curDestination, Time.deltaTime * moveSpeed);

    }
}
